#!/usr/bin/env python
# _*_ coding: utf-8_*_
#
# Copyright 2016 planc2c.com
# thomas@time2box.com
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.web
import logging
import time
import sys
import os
import uuid
import smtplib
import json as JSON # 启用别名，不会跟方法里的局部变量混淆
from bson import json_util

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../dao"))

from comm import cur_file_dir
from comm import timestamp_date


# /ui/mateblog/index
class MateblogIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/index.html')


# /ui/mateblog/home-2
class MateblogHome2Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/home-2.html')


# /ui/mateblog/home-3
class MateblogHome3Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/home-3.html')


# /ui/mateblog/home-4
class MateblogHome4Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/home-4.html')


# /ui/mateblog/home-5
class MateblogHome5Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/home-5.html')


# /ui/mateblog/single-left-sidebar
class MateblogSingleLeftSidebarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/single-left-sidebar.html')


# /ui/mateblog/single
class MateblogSingleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/single.html')


# /ui/mateblog/about
class MateblogAboutHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/about.html')


# /ui/mateblog/contact
class MateblogContactHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('mateblog/contact.html')
