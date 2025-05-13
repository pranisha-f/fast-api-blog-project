from fastapi import FastAPI
from core.configg import settings
from apis.base import api_router
from apps.base import app_router

# def create_tables():
#     # Create the database tables if they don't exist
#     Base.metadata.create_all(bind=engine) 
def start_app():
    app=FastAPI(title = settings.PROJECT_TITLE,version = settings.PROJECT_VERSION)
    # Create the database tables when the application starts
    # create_tables()
    # Include the API router
    app.include_router(api_router)
    app.include_router(app_router)
    return app

app = start_app()

# @app.get("/")
# def hello():
#     return {"msg" : "Hi there 👍.This is a blog!"}



