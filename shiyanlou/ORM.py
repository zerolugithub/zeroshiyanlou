#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:16
# @Author  : zero
# @File    : ORM.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

engine = create_engine('mysql://gslbquery:OGNkNGUyZmM3ZWE@10.11.173.27:3860/test?charset=utf8')
Base = declarative_base(engine)
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, index=True)
    def __repr__(self):
        return '<User: {}>'.format(self.name)

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='course')
    def __repr__(self):
      return '<Course: {}>'.format(self.name)

Base.metadata.create_all()
u1 = User(name='Kobe')
u2 = User(name='Nash')
u3 = User(name='James')
c1 = Course(name='Mysql 基础', user=u1)
c2 = Course(name='Flask-SQLAlchemy 快速入门', user=u1)
for i in (u1, u2, u3, c1, c2):
    session.add(i)
session.commit()

print(c1.user)
print(c2.user)


