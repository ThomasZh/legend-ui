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


# /ui/editor
class EditorIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/index.html')


# /ui/editor/popular/full
class EditorPopularFullHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/full.html')


# /ui/editor/popular/toolbar_inline
class EditorPopularToolbarInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/toolbar_inline.html')


# /ui/editor/popular/two_instances
class EditorPopularTwoInstancesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/two_instances.html')


# /ui/editor/popular/textarea
class EditorPopularTextareaHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/textarea.html')


# /ui/editor/popular/full_page
class EditorPopularFullPageHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/full_page.html')


# /ui/editor/popular/iframe
class EditorPopularIframeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/iframe.html')


# /ui/editor/popular/disable_edit
class EditorPopularDisableEditHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/disable_edit.html')


# /ui/editor/popular/z_index
class EditorPopularZindexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/z_index.html')


# /ui/editor/popular/init_on_click
class EditorPopularInitOnClickHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/init_on_click.html')


# /ui/editor/popular/toolbar_buttons
class EditorPopularToolbarButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/toolbar_buttons.html')


# /ui/editor/popular/disable_paragraphs
class EditorPopularDisableParagraphsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popular/disable_paragraphs.html')


# /ui/editor/3rd-party/aviary/index
class Editor3rdPartyAviaryIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/aviary/index.html')
