# Pacebook
## Video Demo: https://youtu.be/PBf77gMblnE
## Description

***Pacebook - social media platform for football (soccer) drills***

**Pacebook users can explore football drills posted by others, as well as post their own drills for others to see**


*I used multiple languages in this project: SQL, Python, Jinja, JavaScript, HTML, CSS. All of these languages played a big role in the software, but I would take the most pride in the JavaScript that I implemented in Pacebook, as it was the language that took the most time for me to figure out, but also I was able to achieve my best features using it.*

### Folders and Files

#### */website*
This folder contains all of the files related to the website software it self. In fact, planning.txt and README.md are the only files which are not in /website.

#### /website/flask_session
This folder contains a record of all the flask sessions

#### /website/static
This folder contains a sub-folder called '/images' which contains all of the images used for the drills, and it is also where the images uploaded by users go to.

It also contains my three .js files: add_drill.js, favorites.js, and index.js, as well as styles.css.

#### /website/static/index.js
This file is linked to index.html and is responsible for the 'Add to favorites' buttons' behaviour, as well as the search bar. I also implement JS from here to the 'fullview' button, because when clicking on a fullview button of any drill, the link to that page is unique because it has a /'x' at the end, and the x is the drill's id in my SQL database.

#### /website/static/favorites.js
This file is linked to the favorites.html file, and it copies two functions from index.js as the funcitonality is really the same. The onyl difference is that when I press 'Remove from favorites' in favorites.html, unlike index.html where the drill would be removed from favorties without a reload, there is a refresh of the page, after which that drill is not there anymore. I chose to have a refresh of the page because it didn't make much sense to keep the drill in favorites.html if it is not actually there anymore

#### /website/static/add_drill.js
This file is linked to the add_drill.html file, and it only has one event listener, which waits for the user to upload an image to the page. I had to implement this event listener for 2 outcomes:
1) The image that the user uploads to the input box gets saved in /static/images, so that it can later be found in the website.db database to be displayed later on in the website when the drill is added.
2) A blue spinner would pop up while the image was loading, so that the user would not awkwardly wait for their image to show up on the page.


#### /website/templates
This folder contains all of my .html files.

#### /website/templates/layout.html
This file is the layout file for all of my other html files (just like taught in week 8 or 9). This file has 3 block: title, head, and main. The title block changes the title of the page on the tab. The head block is there in case if I want to link something from bootstrap on a specific page. Block main is everything else. layout.html is mainly used to preserve the navbar on all pages, as well as the footer. Also you will see the Jinja code that I used in the navbar block. This ensures that if a user is not logged in, all they see on their navbar is the Pacebook, login and register buttons.

#### /website/templates/login.html and register.html
Both of these files contains forms to log or register the user into the website, that are then sent to and processed by app.py

#### /website/templates/index.html
This file is the main page in my website (catalogue). I used Jinja syntax here to display all of the drills in my SQLite database. The user can see all of the drills on this page. They can also add any drill to favorites, as well as remove any drill that they have added, from this page. There is also a search bar in between the heading and the feed of drills, in which the user can type text, and the drills will be sorted by which drills match the title or the username of that inputted text.

#### /website/templates/fullview.html
This is the page that is displayed when the user presses on any fullview button in index.html or favorites.html. This page displays all information about a drill in a user-friendly way, because there is an icon next to each piece of information. If the user does not undestand what a certain piece of information means in the table, they can hover over the icon and there will be text that pops up such as 'Skill' or 'Position', explaining what the information is about. There is also a 'Watch Video' button on the drills that have a video linked to them, and if the user clicks on the button, they will see a popup of the video, which lets them watch the video without exiting the website.

#### /website/templates/favorites.html
This page displays all of the drills that the user has marked as favorite. The functionality for a drill card is the same as index.html. The only difference is that the page is reloaded after the user removes a drill from favorites, while on index.html that process happens without a reload.

#### /website/templates/add_drill.html
This html file is the 'Add a Drill' page. It is mostly one big form, which consists of mostly text inputs, one image upload input, and a radio button input. I take the most pride in the image upload feature on this page, as it took some time to implement, but this implementation was mostly done in its JS file.

#### /website/app.py
This file is the backend of Pacebook. It is responsible for all the app routes, including all the logic that happened behind the scenes. Overall, I had the most enjoyment working in this file, because I found the backend of Pacebook very fun to make!

#### /website/website.db
This is the database that I used for Pacebook. It has three tables: drills, favorites, users. **drills** is a table for all of the drills shown on the website at any given moment. **users** is a table for all of the registered users on Pacebook. **favorites** is a table for all drills that any user has listed as their favorites. Many drills in favorites are obviously the same as two users can list the same drill as their favorite, but the identifier for who liked a certain drill in the table is the 'user_id' field.

#### planning.txt
This is a simple .txt file that I used for inserting into website.db, which made it easier for me to write the prompts.

### Design choices and experiences
There were many debates that I had with myself throughout the project, so I will talk about a couple. One of the debates was whether I should make the event of adding a drill to favorites result in a reload of the page, to make the process of coding the website easier for me. The current version of Pacebook shows that I did not go with this, and that I actually added JS to make it so that the button is added without a reload (app.py is also crucial in this because I added two routes that handled adding and removing drills from a users favorites').

Another debate that I had wasn't as much of a debate as it was a matter of not giving up. When I first thought about implementing a video of each drill in the website, I immediately thought about a video popup. I found many sources which suggested how to implement a popup, but ended up liking Magnific Popup's the most, mainly because of the visual simplicity that it had. When I tried use it in my code, it would always keep sending me to YouTube with that link. Then when I fixed that, either the video would not play or there would be issues with the sound. At that point I felt so frustrated trying so hard on a fairly small feature that I thought about just making it so that when the user presses on the 'Watch Video' button, they just open the YouTube link and watch it on YouTube. But after some time, I realized that this 'Watch Video' feature was more important to me, and I decided to play around with the code and see what happens for a few days. After switching around the order of the Magnific Popup scripts, the feature actually worked. I felt so proud of myself that I did not give up on the feature and that I actually made it work. Without a doubt, this was one of my favorite moments throughout the whole project.

