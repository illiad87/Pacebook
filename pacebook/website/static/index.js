document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');

    searchInput.addEventListener('input', function(event) {
        const searchValue = event.target.value.toLowerCase();
        all_drills.forEach((drill) => {
            const cardElements = document.getElementsByClassName('card');
            Array.from(cardElements).forEach((card) => {
                const title = card.querySelector('.card-title').innerText.toLowerCase();
                const isVisible = title.includes(searchValue);

                card.style.display = isVisible ? 'block' : 'none';
            });
        });
    });
});


function add_to_favorites (drill_id)
{
    var id = `${drill_id}`
    const favorites_button = document.getElementById(`unadded_fav${drill_id}`)
    console.log(favorites_button)

    var xhr = new XMLHttpRequest()
    xhr.open('POST', '/add_to_favorites', true)
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.send('drill_id=' + id)
    favorites_button.setAttribute("onclick", `remove_from_favorites('${drill_id}')`)
    favorites_button.setAttribute("id", `added_fav${drill_id}`)
    favorites_button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-check" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/> <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/> </svg> Remove from favorites'
}


function remove_from_favorites(drill_id)
{
    var id = `${drill_id}`
    const favorites_button = document.getElementById(`added_fav${drill_id}`)
    console.log(favorites_button)

    var xhr = new XMLHttpRequest()
    xhr.open('POST', '/remove_from_favorites', true)
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.send('drill_id=' + id)
    favorites_button.setAttribute("onclick", `add_to_favorites('${drill_id}')`)
    favorites_button.setAttribute("id", `unadded_fav${drill_id}`)
    favorites_button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16"> <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/> </svg> Add to favorites'
}

function fullview(drill_id)
{
    var id = `${drill_id}`

    var xhr = new XMLHttpRequest()
    xhr.open('POST', '/fullview', true)
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.open()
            document.write(xhr.responseText)
            document.close()
        }
    }
    xhr.send('drill_id=' + id)
}

