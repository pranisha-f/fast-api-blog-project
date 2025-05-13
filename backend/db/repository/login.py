from sqlalchemy.orm import Session
from core.hashing import Hasher
from db.session import get_db
from db.models.user import User

def get_user_by_email(email:str,db:Session):
  user=db.query(User).filter(User.email==email).first()
  if not user:
    return False
  return user


def authenticate_user(email:str,password:str,db:Session):
  user=db.query(User).filter(User.email==email).first()
  if not user:
    return False
  if not Hasher.verify_password(password,user.password):
    return False
  return user
  
