
function remove_from_favorites(drill_id)
{
    var id = `${drill_id}`;
    const favorites_button = document.getElementById(`added_fav${drill_id}`);
    console.log(favorites_button);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/favorites_remove_from_favorites', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('drill_id=' + id);
}

function fullview(drill_id)
{
    var id = `${drill_id}`;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/fullview', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.open();
            document.write(xhr.responseText);
            document.close();
        }
    };
    xhr.send('drill_id=' + id);
}
