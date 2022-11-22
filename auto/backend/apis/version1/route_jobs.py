from fastapi import APIRouter
from typing import List   
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job, retreive_job, list_jobs,update_job_by_id 
from db.repository.jobs import delete_job_by_id

router = APIRouter()


@router.delete("/delete/{id}")
def delete_job(id: int,db: Session = Depends(get_db)):
    current_user_id = 1
    message = delete_job_by_id(id=id,db=db,owner_id=current_user_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} not found")
    return {"msg":"Successfully deleted."}


@router.post("/create-job/",response_model=ShowJob)
def create_job(job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job,db=db,owner_id=current_user)
    return job

@router.get("/all",response_model=List[ShowJob]) #new
def read_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs

@router.get("/get/{id}", response_model=ShowJob
)  # if we keep just "{id}" . it would stat catching all routes
def read_job(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {id} does not exist",
        )
    return job
 
@router.put("/update/{id}")   #new
def update_job(id: int,job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    message = update_job_by_id(id=id,job=job,db=db,owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} not found")
    return {"msg":"Successfully updated data."}