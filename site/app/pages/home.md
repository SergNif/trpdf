# Перевести PDF

Переводите PDF документы с английского на русский.
Документ переводится с помощью нейросети. Поэтому в переведенном тексте возможны неточности. Чтобы было удобно сравнить перевод с оригиналом, текст переводится по каждому абзацу. Ограничений на размер файла нет. Ограничений на количество переводов нет.

Есть ограничение, связанное с ограниченным объемом хостинга. Нет места для хранения файлов. Поэтому есть возможность только отправить переведенный документ сразу на вашу электронную почту. После этого оба файла немедленно удаляются с сервера.



<html>
<head>
    <title>Some Upload Form</title>
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <!-- <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" /> -->

<!--   <title>Drag and Drop File Upload using DropzoneJS Python Flask PostgreSQL</title>   -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="/static/css/dropzone.css" />
<script type="text/javascript" src="/static/js/dropzone.js"></script>
<!--      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous"> -->


</head>
<body>
    <p><b>Enter yuor mail for link for download translated document:<b><Br></p>
    <input name="email" type="text" id="control_e_mail" autocomplete="off" required placeholder="e-mail"/>
    <!-- <input  name="mail_name" type="text" value='e-mail' id="control_e_mail" /> -->
    <p><br><br><br></p>
    <p></p>
    <p id="Email">Your mail: </p>
    <!-- <ul id='messagesMM'>
    </ul> -->
    <p></p>
        <div class="container" id="container_drop"> 
                <div class="dz-message needsclick">
        <form action="/uploadfiles" class="dropzone" id="my-great-dropzone">
        <!-- <input  name="mail_name{{ loop.index }}" type="text" value='sd@sa.io' /> -->
                                    <label for="upload_costum"  class="upload_label">
                    <div class="image">
                        <img src="" alt="">
                    </div>
                    <i class="fas fa-cloud-upload-alt"></i>
                    </label>
                        <img alt="Dropzone.js" src="https://raw.githubusercontent.com/dropzone/dropzone/assets/github-logo.svg" />
    <!-- <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"> -->
    <!-- <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script> -->
    <!-- JavaScript Bundle with Popper -->
	<!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script> -->
	<!-- JQuery -->
	<!-- <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> -->
	<!-- <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> -->
    <!-- <script type='text/javascript' src="../static/js/autocomplete.js"></script>> -->
    <!-- <markdown <script src="{{ url_for('static', path='js/autocomplete.js') }}"></script>></<markdown> -->
    <!-- <input type="email" name="mail_name2" value="" /> -->
       <script>
        Dropzone.options.myGreatDropzone = { // camelized version of the `id`
            paramName: "upload", // The name that will be used to transfer the file
            parallelUploads: 10, // Number of parallel upload
            maxFiles: 10,
            maxFilesize: 450, // MB
        };
    </script>
                </form>
                    </div>
    </div>
    <!--     <form class="d-flex" action="/search/">
            <input class="form-control me-2" id="autocomplete" name="query" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form> -->

</body>
</html>

This project uses [FastAPI](https://fastapi.tiangolo.com/), [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/), and [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/).

