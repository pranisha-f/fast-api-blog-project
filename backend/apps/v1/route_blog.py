from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
router=APIRouter()

@router.get("/")
def home(request:Request):
    return templates.TemplateResponse("blogs/home.html",{"request":request})


