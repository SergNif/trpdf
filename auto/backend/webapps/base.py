from webapps.jobs import route_jobs
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_jobs.router, prefix="", tags=["job-webapp"])
