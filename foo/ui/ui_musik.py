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


# /ui/musik/index
class MusikIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/index.html')


# /ui/musik/genres
class MusikGenresHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/genres.html')


# /ui/musik/events
class MusikEventsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/events.html')


# /ui/musik/listen
class MusikListenHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/listen.html')


# /ui/musik/video
class MusikVideoHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/video.html')


# /ui/musik/video-detail
class MusikVideoDetailHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/video-detail.html')


# /ui/musik/layout-color
class MusikLayoutColorHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/layout-color.html')


# /ui/musik/layout-boxed
class MusikLayoutBoxedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/layout-boxed.html')


# /ui/musik/layout-fluid
class MusikLayoutFluidHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/layout-fluid.html')


# /ui/musik/buttons
class MusikButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/buttons.html')


# /ui/musik/icons
class MusikIconsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/icons.html')


# /ui/musik/grid
class MusikGridHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/grid.html')


# /ui/musik/widgets
class MusikWidgetsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/widgets.html')


# /ui/musik/components
class MusikComponentsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/components.html')


# /ui/musik/list
class MusikListHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/list.html')


# /ui/musik/table-static
class MusikTableStaticHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/table-static.html')


# /ui/musik/table-datatable
class MusikTableDatatableHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/table-datatable.html')


# /ui/musik/form-elements
class MusikFormElementsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/form-elements.html')


# /ui/musik/form-validation
class MusikFormValidationHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/form-validation.html')


# /ui/musik/form-wizard
class MusikFormWizardHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/form-wizard.html')


# /ui/musik/chart
class MusikChartHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/chart.html')


# /ui/musik/portlet
class MusikPortletHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/portlet.html')


# /ui/musik/timeline
class MusikTimelineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/timeline.html')


# /ui/musik/profile
class MusikProfileHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/profile.html')


# /ui/musik/blog
class MusikBlogHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/blog.html')


# /ui/musik/invoice
class MusikInvoiceHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/invoice.html')


# /ui/musik/gmap
class MusikGmapHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/gmap.html')


# /ui/musik/jvectormap
class MusikJvectormapHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/jvectormap.html')


# /ui/musik/signin
class MusikSigninHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/signin.html')


# /ui/musik/signup
class MusikSignupHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/signup.html')


# /ui/musik/404
class Musik404Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/404.html')


# /ui/musik/docs
class MusikDocsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/docs.html')


# /ui/musik/modal-lockme
class MusikModalLockmeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('musik/modal.lockme.html')
