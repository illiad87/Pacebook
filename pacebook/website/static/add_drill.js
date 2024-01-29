
document.addEventListener('DOMContentLoaded', (event) => {
    let drill_image = document.getElementById('drill_image');
    let input_file = document.getElementById('image_input');
    let spinner = document.getElementById('image_upload_spinner');

    input_file.onchange = function () {
        let file = this.files[0];
        let formData = new FormData();
        formData.append('file', file);

        spinner.style.display = 'block';

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            drill_image.src = '/static/images/' + data.filename;
            drill_image.style.border = '1px solid black';
            document.getElementById('image_filename').value = data.filename;
            spinner.style.display = 'none';
        })
        .catch(error => {

            console.error('Error:', error);

            spinner.style.display = 'none';
        });
    }
});
