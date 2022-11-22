from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from apis.base import api_router #new
from db.session import engine   #new
from db.base import Base  #new
from apis.base import api_router
# from webapps.base import api_router as web_app_router #new


# def include_router(app):   
# 	app.include_router(api_router) #modified

# def include_router(app):
# 	app.include_router(general_pages_router)


def include_router(app):
    app.include_router(api_router)
    # app.include_router(web_app_router)  #new

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():           #new
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()       #new
	return app

app = start_application()


if __name__ == '__main__':
    import uvicorn
    import os
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True
    )