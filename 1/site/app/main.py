import mimetypes
import os
import aiofiles
import json
import re
from typing import Optional
from typing import Union

from fastapi import (
    Cookie,
    Depends,
    Query,
    WebSocket,
    WebSocketException,
    status,
)

from fastapi import FastAPI, File, UploadFile, Request, Form, Response
# from wtforms import StringField
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from library.helpers import *
from routers import upload, twoforms, unsplash, accordion
from dotenv import load_dotenv
import config

from dotenv import load_dotenv
load_dotenv()

# from time import datetime

mimetypes.init()

html = """ 
<html>
<head>
    <title>Some Upload Form</title>
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" />
</head>
<body>
    <form action="/uploadfiles" class="dropzone" id="my-great-dropzone">
    </form>
    <script>
        Dropzone.options.myGreatDropzone = { // camelized version of the `id`
            paramName: "uploaded_files", // The name that will be used to transfer the file
            maxFilesize: 2, // MB
        };
    </script>
</body>
</html>
"""

app = FastAPI()

app.include_router(upload.router)
app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)

templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="/home/serg/python311_proj/fastapi/static"), name="static")

mimetypes.add_type('application/javascript', '.js')
print(f'{os.getcwd()=}')

app.mount("/static", StaticFiles(directory="static"), name="static")
# os.system('python app/inotify__pp.py')


@app.get("/form")
async def present_form():
    print(f'form ********')
    return HTMLResponse(html)

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     data = {
#         "page": "Home page"
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})


# @app.get("/page/{page_name}", response_class=HTMLResponse)
# async def page(request: Request, page_name: str):
#     data = {
#         "page": page_name
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})

# **********************************************
UPLOAD_FOLDER = config.UPLOAD_FOLDER[0]  # f"{os.getcwd()}/uploadfiles/"
# config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# **********************************************


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # form = SearchForm(request.form)
    data = openfile("home.md")
    print(f'home')
    # return templates.TemplateResponse("upload.html", {"request": request, "data": data})
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    data = openfile(page_name+".md")
    print(f'show page')
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

# @app.route("/upload",methods=["POST","GET"])
# def upload():
#     # cursor = mysql.connection.cursor()
#     # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     if Request.method == 'POST':
#         file = Request.files['file']
#         filename = secure_filename(file.filename)
#         now = datetime.now()

#         if file and allowed_file(file.filename):
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         #    cur.execute("INSERT INTO uploads (file_name, upload_time) VALUES (%s, %s)",[file.filename, now])
#         #    mysql.connection.commit()
#         #    cur.close()
#            print('File successfully uploaded ' + file.filename + ' to the database!')
#         else:
#            print('Invalid Uplaod only txt, pdf, png, jpg, jpeg, gif')
#         msg = 'Success Uplaod'
#     return jsonify(msg)


@app.post("/uploadfiles")
async def create_upload_files(upload: list[UploadFile], mail_name: str = Form(...)):
    print(f'{os.getcwd()=} \n {UPLOAD_FOLDER=}')
    print(f'{mail_name=}')
    for file in upload:
        async with aiofiles.open(f"{UPLOAD_FOLDER}{file.filename}", "wb") as out_file:
            content = await file.read()
            # st = await magic.from_file(out_file.name)
            # if ("PDF document" in st ):

            await out_file.write(content)
        print(f"File uploaded: {file.filename}")
    return {"file_name": upload}


@app.get("/search/")
def search(
    request: Request, query: Optional[str] = None
):
    jobs = search_job(query)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request}
    )


@app.get("/autocomplete")
def autocomplete(term: Optional[str] = None):
    print(f'autocomplete {type(term)=} ')
    jobs = search_job(term)
    # job_titles = []
    # for job in jobs:
    #     job_titles.append(job.title)
    # return job_titles
    return {"input": term}


def search_job(query: str):
    jobs = "NO"
    if re.match("[^@]+@[^@]+\.[^@]+", query):
        jobs = query + "OK"
    print(f'{jobs=}')
    return {"search": jobs}


# create_upload_files(uploaded_files: list[UploadFile]):
#     print(f'upload')
#     for file in uploaded_files:
#         async with aiofiles.open(f"app/upload/{file.filename}", "wb") as out_file:
#             content = await file.read()
#             await out_file.write(content)
#         print(f"File uploaded: {file.filename}")
# class SearchForm(Form):
#     autocomp = StringField('Insert City', id='city_autocomplete')

# @app.route('/_autocomplete', methods=['GET'])
# def autocomplete():
#     cities = ["Olongapo City",
#           "Angeles City",
#           "Manila",
#           "Makati",
#           "Pasig",
#           "Davao",
#           "Cebu",
#           "Quezon City",
#           "Taguig"]
#     print(cities)
#     return Response(json.dumps(cities), mimetype='application/json')


if __name__ == '__main__':
    import uvicorn
    import os
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8080,
        reload=True
    )




# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# from .library.helpers import *
# from app.routers import twoforms, unsplash, accordion


# app = FastAPI()


# templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="static"), name="static")

# app.include_router(unsplash.router)
# app.include_router(twoforms.router)
# app.include_router(accordion.router)


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     data = openfile("home.md")
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})


# @app.get("/page/{page_name}", response_class=HTMLResponse)
# async def show_page(request: Request, page_name: str):
#     data = openfile(page_name+".md")
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})
