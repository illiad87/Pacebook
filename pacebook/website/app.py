from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///website.db")

@app.route("/")
def index():
    if not session.get("user_id"):
        return redirect("/login")
    drills = db.execute("SELECT * FROM drills")
    first_drill = drills[0]
    favorites_ids = [d['drill_id'] for d in db.execute("SELECT drill_id FROM favorites")]

    return render_template("index.html", drills=drills, favorites=favorites_ids)


@app.route("/register", methods=["GET", "POST"])
def register():
    # clear the cookies
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        if not username:
            flash("Username cannot be empty")
            return render_template("register.html")
        if not password or not password_confirm:
            flash("Password cannot be empty")
            return render_template("register.html")
        if password != password_confirm:
            flash("Passwords must match")
            return render_template("register.html")

        if len(db.execute("SELECT username FROM users WHERE username == (?)", username)) != 0:
            flash("Username is already taken")
            return render_template("register.html")

        hashed_pw = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash_pw) VALUES (?, ?)", username, hashed_pw)

        session["user_id"] = db.execute("SELECT id FROM users WHERE username == (?)", username)[0]["id"]
        session["username"] = username

        return redirect("/")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        # validate name and pw
        username = request.form.get('username')
        password = request.form.get('password')
        if not username:
            flash("Username cannot be empty")
            return render_template("login.html")

        if not password:
            flash("Password cannot be empty")
            return render_template("login.html")

        user_db = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(user_db) != 1 or not check_password_hash(user_db[0]["hash_pw"], password):
            flash("Invalid username or password")
            return render_template('login.html')

        session["user_id"] = user_db[0]["id"]
        session["username"] = username


        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have successfully been logged out")
    return render_template("login.html")


@app.route("/fullview/<int:drill_id>")
def fullview(drill_id):
    if not session.get("user_id"):
        return redirect("/login")
    drills = db.execute("SELECT * FROM drills WHERE id == (?)", drill_id)
    drill = drills[0]
    return render_template("fullview.html", drill=drill)


@app.route("/add_to_favorites", methods=["POST"])
def add_to_favorites():
    drill_id = request.form['drill_id']
    db.execute("INSERT INTO favorites (drill_id, user_id) VALUES (?, ?)", drill_id, session['user_id'])
    return f"Added to favorites drill {drill_id} from user {session['user_id']}"


@app.route("/remove_from_favorites", methods=["POST"])
def remove_from_favorites():
    drill_id = request.form['drill_id']
    db.execute("DELETE FROM favorites WHERE drill_id == (?) AND user_id == (?)", drill_id, session['user_id'])
    return f"Removed from favorites drill {drill_id} from user {session['user_id']}"


@app.route("/favorites", methods=["GET", "POST"])
def favorites():
    if not session.get("user_id"):
        return redirect("/login")
    if request.method == "POST":
        drill_to_remove_id = request.form['drill_id']
        db.execute("DELETE FROM favorites WHERE drill_id == (?) AND user_id == (?)", drill_to_remove_id, session['user_id'])

    favorites = db.execute("SELECT * FROM favorites WHERE user_id == (?)", session['user_id'])
    favorites_ids = [fav['drill_id'] for fav in favorites]
    drills = db.execute("SELECT * FROM drills WHERE id IN (?)", favorites_ids)
    return render_template("favorites.html", drills=drills, favorites=favorites_ids)

@app.route("/add_drill", methods=["GET", "POST"])
def add_drill():
    if not session.get("user_id"):
        return redirect("/login")
    if request.method == "POST":
        username = session['username']
        image_filename = f"/static/images/{request.form['image_filename']}"
        title = request.form['title']
        description = request.form['description']
        if not request.form['position']:
            position = "Any"
        else:
            position = request.form['position']
        skill = request.form['skill']
        objective = request.form['objective']
        difficulty = request.form['difficulty']
        number_of_players = request.form['number_of_players']
        equipment = request.form['equipment']
        dimensions = request.form['dimensions']
        duration = request.form['duration']
        if not request.form['youtube_link']:
            youtube_link = "None"
        else:
            youtube_link = request.form['youtube_link']
        db.execute(f'''INSERT INTO drills (name, description,
        position, skill, objective,
        image_file_name, difficulty, video_file_name, number_of_players,
        equipment, field_dimensions, duration, username) VALUES (
        '{title}', '{description}', '{position}', '{skill}', '{objective}',
        '{image_filename}', '{difficulty}', '{youtube_link}', '{number_of_players}', '{equipment}', '{dimensions}', '{duration}', '{username}') ''')
        return redirect("/")

    return render_template("add_drill.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('static', 'images', filename))
        return {'filename': filename}, 200
