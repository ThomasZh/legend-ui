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


class IcarusIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('icarus/index.html')


class IcarusCategoryArticlesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('icarus/category_articles.html')


class IcarusCategoriesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('icarus/categories.html')


class IcarusTagsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('icarus/tags.html')


class IcarusSingleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('icarus/single.html')
