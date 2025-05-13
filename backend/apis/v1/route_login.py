from fastapi import APIRouter, Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm ,OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.login import authenticate_user,get_user_by_email
from jose import jwt,JWTError
from core.security import create_access_token
from core.configg import settings
from apis.utils import OAuth2PasswordBearerWithCookie
from fastapi import Response
router=APIRouter()

@router.post("/token")
def login(response:Response,formdata:OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
  user=authenticate_user(formdata.username,formdata.password,db)
  print(user)
  if not user:
    raise HTTPException(detail="Incorrect email or password",status_code=status.HTTP_401_UNAUTHORIZED)
  access_token=create_access_token(data={"sub":user.email})
  response.set_cookie(key="access_token",value=f"Bearer {access_token}",httponly=True)
  print(access_token)
  return {"access-token":access_token,"token-type":"bearer"}

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/token")


def get_current_user(token :str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
  exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED  , detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"},)
  try:
    payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    print(payload)
    email: str =payload.get("sub")
    print(email)
    if email is None:
      raise exception
  except JWTError:
    raise exception
  user = get_user_by_email(email=email,db=db)
  if user is None:
    raise exception
  return user

