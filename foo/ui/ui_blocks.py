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


# /ui/blocks
class BlocksIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/index.html')


# /ui/blocks/call_to_action
class BlocksCallToActionHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/call_to_action.html')


# /ui/blocks/contacts
class BlocksContactsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/contacts.html')


# /ui/blocks/contents
class BlocksContentsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/contents.html')


# /ui/blocks/features
class BlocksFeaturesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/features.html')


# /ui/blocks/footers
class BlocksFootersHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/footers.html')


# /ui/blocks/forms
class BlocksFormsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/forms.html')


# /ui/blocks/headers
class BlocksHeadersHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/headers.html')


# /ui/blocks/pricings
class BlocksPricingsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/pricings.html')


# /ui/blocks/teams
class BlocksTeamsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/teams.html')


# /ui/blocks/testimonials
class BlocksTestimonialsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('blocks/testimonials.html')
