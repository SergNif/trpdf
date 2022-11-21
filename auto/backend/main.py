from apis.base import api_router
from webapps.base import api_router as web_app_router #new


def include_router(app):
    app.include_router(api_router)
    app.include_router(web_app_router)  #new
