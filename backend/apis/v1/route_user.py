from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserCreate, UserResponse
from db.repository.user import create_user_in_db


router = APIRouter()

@router.post("/",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user_in_db(db=db, user=user)
    return db_user
