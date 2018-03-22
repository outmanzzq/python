#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 不懂！！！

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:root@localhost/test",
                       encoding='utf-8')

Base = declarative_base()  # 生成orm基类

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", backref="addresses")  # 这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


