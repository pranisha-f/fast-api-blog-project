from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status,HTTPException
from db.session import get_db
from typing import List
from db.models.user import User
from schemas.blog import CreateBlog,ShowBlog,UpdateBlog
from db.repository.blog import create_blog_in_db, show_blog_in_db, update_blog_in_db,delete_blog_in_db
from apis.v1.route_login import get_current_user

router = APIRouter()

@router.post("/", response_model= ShowBlog,status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    db_blog = create_blog_in_db(db=db, blog=blog, author_id=2)
    return db_blog

@router.get("/{id}", response_model= ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db)):
    db_blog = show_blog_in_db(db=db, id= id)
    if not db_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return db_blog

@router.put("/{id}", response_model= ShowBlog)
def update_blog(id:int ,blog: UpdateBlog,db: Session = Depends(get_db),current_user: User=Depends(get_current_user)):
    blogs = update_blog_in_db(id=id,db=db, blog=blog, author_id=current_user.id)
    if isinstance(blogs,dict):
      raise HTTPException(detail=blogs.get("error"),status_code=status.HTTP_400_BAD_REQUEST)
    return blogs

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db),current_user: User=Depends(get_current_user)):
    print("delete operation")
    msg = delete_blog_in_db(id=id, db=db,author_id=current_user.id)
    if msg.get("error"):
        raise HTTPException(detail=msg.get("error"),status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg":msg.get("msg")}