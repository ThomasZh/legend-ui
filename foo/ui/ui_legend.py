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


class LegendIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/moments.html')


class LegendArticleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/article.html')


class LegendProductHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/product.html')


class LegendProductPlaceOrderHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/place-order.html')


class LegendProductPlaceOrderSuccessHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/place-order-success.html')


class LegendMomentHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/moment.html')


class LegendAddMomentHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/add-moment.html',
            club_id="1")


class LegendAddCommentHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('legend/add-comment.html',
            club_id="1")
