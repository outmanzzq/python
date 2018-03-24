#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

from sqlalchemy import Table, Column, Integer, String, Enum, DATE, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__ = 'remote_user'
    id = Column(Integer, primary_key=True)

    AuthTypes = [
        ('ssh-password', 'SSH/Password'),
        ('ssh-key', 'SSH/KEY')
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username


class BindHost(Base):
    '''
    192.168.1.11 web   bj_group
    192.168.1.11 mysql sh_group
    192.168.1.11 mysql sh_group
    '''
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('host_id', 'group_id', 'remote_id'))

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship("Host", backref="bind_hosts")
    group = relationship("HostGroup", backref="bind_hosts")
    remote_user = relationship("RemoteUser", backref="bind_hosts")

    def __repr__(self):
        return "<%s -- %s -- %s" % (self.host.ip,
                                    self.remote_user.username,
                                    self.group.name)


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
    bing_hosts = relationship("BindHost", secondary="user_m2m_bindhost", backref='user_profiles')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    pass




