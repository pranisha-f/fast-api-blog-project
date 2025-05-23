from db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    author_id =  Column(Integer,ForeignKey("user.id"))
    author = relationship("User",back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    
