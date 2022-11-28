# Перевести PDF

Переводите PDF документы с английского на русский.
Документ переводится с помощью нейросети. Поэтому в переведенном тексте возможны неточности. Чтобы было удобно сравнить перевод с оригиналом, текст переводится по каждому абзацу. Ограничений на размер файла нет. Ограничений на количество переводов нет.

Есть ограничение, связанное с ограниченным объемом хостинга. Нет места для хранения файлов. Поэтому есть возможность только отправить переведенный документ сразу на вашу электронную почту. После этого оба файла немедленно удаляются с сервера.

<html>
<head>
    <title>Some Upload Form</title>
    <!-- <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" /> -->

<!-- <link href="//code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" rel="Stylesheet"></link>
<script src="//code.jquery.com/jquery-2.2.0.min.js"></script>
<script src="//code.jquery.com/ui/1.10.2/jquery-ui.js" ></script> -->

<!-- <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> -->
  
</head>
<body>
    <title>Some Upload Form</title>


<!-- <script type='text/javascript' src="/home/serg/python311_proj/fastapi/site/static/js/autocomplete.js"></script> -->

<!--
<script type="text/javascript" src="/home/serg/python311_proj/fastapi/site/static/js/autocomplete.js"></script>


    <div>
        <input name="fcomp" type="text" id="fcomp" class="form-control input-lg"/>
    </div>



    <input type="email" name="mail_name2" value="" />
    </form> -->

        <p id="Email">Enter yuor mail for link for download translated document</p>



<!-- <script type="text/javascript" src="/home/serg/python311_proj/fastapi/site/static/js/autocomplete.js"></script> -->
        <!-- <form class="d-flex" action="/search/">
            <input class="form-control me-2" id="autocomplete" name="query" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form> -->


 <!-- <form action="/autocomplete" autocomplete="on"> -->
  
<!-- <input class="form-control me-2" name="query" id="autocomplete" type="search" placeholder="Search" aria-label="Search"> -->
            <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
  
  
<!-- </form>  -->


<!-- <input type="file" accept="application/pdf">
    <script>
        Dropzone.options.myGreatDropzone = { // camelized version of the `id`
            paramName: "upload", // The name that will be used to transfer the file
            parallelUploads: 10, // Number of parallel upload
            maxFiles: 10,
            maxFilesize: 450, // MB
        };
    </script>
    </input>
    <form action="/uploadfiles" class="dropzone" id="my-great-dropzone"> -->
    <input  name="mail_name{{ loop.index }}" type="text" value='' />

</body>
</html>

This project uses [FastAPI](https://fastapi.tiangolo.com/), [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/), and [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/).
