#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:root@localhost/test",
                       encoding='utf-8')

Base = declarative_base()  # 生成orm基类

class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<id: %s name: %s>" % (self.id, self.name)


Base.metadata.create_all(engine)  # 创建表结构


session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = session_class()  # 生成session实例

# --- 插入数据 ---
# user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
# user_obj2 = User(name="jack", password="alex3714")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# session.add(user_obj2)
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
# session.commit()  # 现此才统一提交，创建数据

# --- 查询 ---
# my_user = session.query(User).filter(User.id>2).filter(User.id<7).first()
# print(my_user)
#
# my_user.name = "Jack Liu"
# my_user.password = "123456"

# --- 回滚 ---
# fake_user = User(name='Rain', password='12345')
# session.add(fake_user)
#
# # print(session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
# print(session.query(User).filter(User.name.in_(['Jack', 'rain'])).count())  # 这时看session里有你刚添加和修改的数据

# session.rollback()  # 此时你rollback一下
# session.commit()

from sqlalchemy import func

print(session.query(func.count(User.name), User.name).group_by(User.name).all())


