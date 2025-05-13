from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.models.blog import Blog

def create_blog_in_db(db: Session, blog: CreateBlog, author_id: int):
    db_blog = Blog(title=blog.title,content=blog.content, author_id=author_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def show_blog_in_db(db: Session, id: int):
    db_blog = db.query(Blog).filter(Blog.id == id).first()
    return db_blog

def update_blog_in_db(id:int, blog: UpdateBlog,db: Session,author_id: int):
    blogs = db.query(Blog).filter(Blog.id == id).first()
    if not blogs:
      return{"error":f"Blog with id {id} not found"}
    if not blogs.author_id==author_id:
      return{"error":f"Only the Blog's author can update the Blog contents."}
         
    blogs.title = blog.title
    blogs.content = blog.content
    blogs.author_id = author_id
    db.add(blogs)
    db.commit()
    # db.refresh(blogs)
    return blogs

def delete_blog_in_db( id: int,db: Session, author_id:int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
      return{"error":f"Blog with {id} not found"}
    if not blog.first().author_id == author_id:
      return{"error":f"Only the Blog's author can delete the Blog contents."}     
    blog.delete()
    db.commit()
    return {"msg":f"Deleted blog with id {id}"}