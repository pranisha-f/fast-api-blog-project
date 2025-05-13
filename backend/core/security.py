from jose import jwt
from datetime import datetime,timedelta
from core.configg import settings


def create_access_token(data:dict):
  encode_data=data.copy()
  expiry_time= datetime.utcnow()+timedelta(minutes=settings.EXPIRY_TIME)
  encode_data.update({"exp":expiry_time})
  encoded_jwt_token=jwt.encode(encode_data,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
  return encoded_jwt_token

