from dotenv import load_dotenv
import os

load_dotenv()   
class Settings:
    PROJECT_TITLE: str = "Blog ✌️"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY:str= os.getenv("SECRET_KEY")
    ALGORITHM= "HS256"
    EXPIRY_TIME= 30

settings = Settings()