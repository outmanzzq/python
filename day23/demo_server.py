#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

from wsgiref.simple_server import make_server
from demo_hello import application

httpd = make_server('', 8000, application)
print('Servering HTTP on port 8000...')

httpd.serve_forever()

