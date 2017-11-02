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


# /ui/newsup/index
class NewsupIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/index.html')


# /ui/newsup/author
class NewsupAuthorHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/author.html')


# /ui/newsup/media
class NewsupMediaHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/media.html')


# /ui/newsup/shortcodes
class NewsupShortcodesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/shortcodes.html')


# /ui/newsup/contact
class NewsupContactHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/contact.html')


# /ui/newsup/account
class NewsupAccountHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/account.html')


# /ui/newsup/item-detail
class NewsupItemDetailHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/item-detail.html')


# /ui/newsup/new
class NewsupNewHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/new.html')


# /ui/newsup/register
class NewsupRegisterHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/register.html')


# /ui/newsup/category
class NewsupCategoryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('newsup/category.html')
