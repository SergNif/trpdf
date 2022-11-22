from fastapi import APIRouter

# from apis.version1 import route_general_pages
from apis.version1 import route_jobs
from apis.version1 import route_users 
from apis.version1 import route_login  #new
# from webapps import base #api_router as web_app_router
from webapps.jobs import route_jobs as web_app_router


api_router = APIRouter()
# api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(web_app_router.router,prefix="",tags=["job-webapp"])
api_router.include_router(route_jobs.router,prefix="/jobs",tags=["jobs"])
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_login.router,prefix="/login",tags=["login"])   #new