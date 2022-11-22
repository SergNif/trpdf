from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.repository.users import create_new_user

from schemas.users import UserCreate,ShowUser  #modified
from db.session import get_db

router = APIRouter()


@router.post("/",response_model = ShowUser) 
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    print(f'route user')
    user = create_new_user(user=user,db=db)
    return user 

