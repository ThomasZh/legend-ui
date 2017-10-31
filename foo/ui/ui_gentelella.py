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


# /ui/gentelella
class GentelellaIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/index.html')


# /ui/gentelella/index2
class GentelellaIndex2Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/index2.html')


# /ui/gentelella/index3
class GentelellaIndex3Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/index3.html')


# /ui/gentelella/form
class GentelellaFormHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form.html')


# /ui/gentelella/form_advanced
class GentelellaFormAdvancedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form_advanced.html')


# /ui/gentelella/form_validation
class GentelellaFormValidationdHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form_validation.html')


# /ui/gentelella/form_wizards
class GentelellaFormWizardsdHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form_wizards.html')


# /ui/gentelella/form_upload
class GentelellaFormUploadHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form_upload.html')


# /ui/gentelella/form_buttons
class GentelellaFormButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/form_buttons.html')


# /ui/gentelella/general_elements
class GentelellaGeneralElementsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/general_elements.html')


# /ui/gentelella/media_gallery
class GentelellaMediaGalleryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/media_gallery.html')


# /ui/gentelella/typography
class GentelellaTypographyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/typography.html')


# /ui/gentelella/icons
class GentelellaIconsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/icons.html')


# /ui/gentelella/glyphicons
class GentelellaGlyphiconsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/glyphicons.html')


# /ui/gentelella/widgets
class GentelellaWidgetsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/widgets.html')


# /ui/gentelella/invoice
class GentelellaInvoiceHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/invoice.html')


# /ui/gentelella/inbox
class GentelellaInboxHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/inbox.html')


# /ui/gentelella/calendar
class GentelellaCalendarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/calendar.html')


# /ui/gentelella/tables
class GentelellaTablesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/tables.html')


# /ui/gentelella/tables_dynamic
class GentelellaTablesDynamicHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('gentelella/tables_dynamic.html')
