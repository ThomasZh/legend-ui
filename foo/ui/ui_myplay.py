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


# /ui/myplay/index
class MyplayIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/index.html')


# /ui/myplay/shows
class MyplayShowsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/shows.html')


# /ui/myplay/history
class MyplayHistoryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/history.html')


# /ui/myplay/movies
class MyplayMoviesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/movies.html')


# /ui/myplay/sports
class MyplaySportsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/sports.html')


# /ui/myplay/news
class MyplayNewsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/news.html')


# /ui/myplay/upload
class MyplayUploadHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/upload.html')


# /ui/myplay/about
class MyplayAboutHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/about.html')


# /ui/myplay/press
class MyplayPressHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/press.html')


# /ui/myplay/copyright
class MyplayCopyrightHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/copyright.html')


# /ui/myplay/creators
class MyplayCreatorsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/creators.html')


# /ui/myplay/developers
class MyplayDevelopersHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/developers.html')


# /ui/myplay/terms
class MyplayTermsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/terms.html')


# /ui/myplay/privacy
class MyplayPrivacyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/privacy.html')


# /ui/myplay/try
class MyplayTryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/try.html')


# /ui/myplay/single
class MyplaySingleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('myplay/single.html')
