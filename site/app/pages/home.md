# Перевести PDF

Переводите PDF документы с английского на русский.
Документ переводится с помощью нейросети. Поэтому в переведенном тексте возможны неточности. Чтобы было удобно сравнить перевод с оригиналом, текст переводится по каждому абзацу. Ограничений на размер файла нет. Ограничений на количество переводов нет.

Есть ограничение, связанное с ограниченным объемом хостинга. Нет места для хранения файлов. Поэтому есть возможность только отправить переведенный документ сразу на вашу электронную почту. После этого оба файла немедленно удаляются с сервера.

<html>
<head>
    <title>Some Upload Form</title>
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" />

</head>
<body>
    <title>Some Upload Form</title>
<!-- <script type="text/javascript" src="{{ url_for('static', filename='/js/autocomplete.js') }}"></script> -->
<!-- <script type="text/javascript" src="/home/serg/python311_proj/fastapi/site/static/js/autocomplete.js"></script> -->
<!-- <input class="search-box" name="query" id="autocomplete" type="text" placeholder="Search" aria-label="Search"> -->
<!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
<p></p>
<p></p>
        <form action="/uploadfiles" class="dropzone" id="my-great-dropzone">

            <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->


<input type="file" accept="application/pdf">
    <script>
        Dropzone.options.myGreatDropzone = { // camelized version of the `id`
            paramName: "upload", // The name that will be used to transfer the file
            parallelUploads: 10, // Number of parallel upload
            maxFiles: 10,
            maxFilesize: 650, // MB
        };
    </script>
    <p id="Email">Enter yuor mail for link for download translated document</p>
    </input>

        </form>

</body>
</html>

This project uses [FastAPI](https://fastapi.tiangolo.com/), [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/), and [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/).
