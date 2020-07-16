from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .db import Base

class Post(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    tags = Column(String)
    toplevel = Column(Integer)
    defunct = Column(Boolean)
    date = Column(Integer)
    