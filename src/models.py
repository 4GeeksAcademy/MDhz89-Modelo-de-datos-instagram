import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

    # Relación para obtener los comentarios del usuario
    comentarios = relationship("Comentarios", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    description = Column(String(250))
    User_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

    # Relación para obtener los comentarios de la publicación
    comentarios = relationship("Comentarios", back_populates="post")

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))  # Cambiar a Integer
    user_id = Column(Integer, ForeignKey('User.id'))  # Cambiar a Integer
    comment = Column(String(250))

    # Relaciones
    user = relationship(User, back_populates="comentarios")
    post = relationship(Post, back_populates="comentarios")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    description = Column(String(250))
    User_id = Column(Integer, ForeignKey('User.id'))
    User_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
