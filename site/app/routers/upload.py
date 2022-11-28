from fastapi import Request, Form, APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from library.helpers import *
from typing import Optional
import re


router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/upload", response_class=HTMLResponse)
def get_upload(request: Request):
    print(f'{"upload"}')
    result = "Hello from upload.py"
    return templates.TemplateResponse('upload.html', context={'request': request, 'result': result})


@router.post("/upload/new/")
async def post_upload(imgdata: tuple, file: UploadFile = File(...)):
    print(f'{file=}')
    data_dict = eval(imgdata[0])
    winWidth, imgWidth, imgHeight = data_dict["winWidth"], data_dict["imgWidth"], data_dict["imgHeight"]

    # create the full path
    workspace = create_workspace()
    # filename
    file_path = Path(file.filename)
    # image full path
    img_full_path = workspace / file_path
    with open(str(img_full_path), 'wb') as myfile:
        contents = await file.read()
        myfile.write(contents)
    # create a thumb image and save it
    thumb(img_full_path, winWidth, imgWidth, imgHeight)
    # create the thumb path
    # ext is like .png or .jpg
    filepath, ext = os.path.splitext(img_full_path)
    thumb_path = filepath + ".thumbnail"+ext

    data = {
        "img_path": img_full_path,
        "thumb_path": thumb_path
    }
    return data

# @router.get("/autocomplete")
# def autocomplete(term: Optional[str] = None, db: Session = Depends(get_db)):
#     jobs = search_job(term, db=db)
#     job_titles = []
#     for job in jobs:
#         job_titles.append(job.title)
#     return job_titles


@router.get("/autocomplete{ght}")
def autocomplete(term: Optional[str] = None, ght: Optional[str]=None):
    print(f'router {ght=}')
    print(f'autocomplete {type(ght)=} ')
    jobs = search_job(term)
    # job_titles = []
    # for job in jobs:
    #     job_titles.append(job.title)
    # return job_titles
    return {"input": term}


def search_job(query: str):
    jobs = "NO"
    print(query)
    if re.match("[^@]+@[^@]+\.[^@]+", query):
        jobs = query + "OK"
    print(f'{jobs=}')
    return {"search": jobs}