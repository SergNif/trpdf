#main.py

from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"msg":"Hello API"}

#from apis.base import api_router
#from webapps.base import api_router as web_app_router #new


#def include_router(app):
#    app.include_router(api_router)
#    app.include_router(web_app_router)  #new
