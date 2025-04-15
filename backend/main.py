from fastapi import FastAPI
from core.configg import settings

app=FastAPI(title = settings.PROJECT_TITLE,version = settings.PROJECT_VERSION)
# app=FastAPI(title = "Blog",version = "0.1.0")

@app.get("/")
def hello():
    return {"msg" : "Hi there 👍.This is a blog!"}
