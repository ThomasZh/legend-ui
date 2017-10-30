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


# /ui/weui
class WeuiIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/index.html')


# /ui/weui/buttons
class WeuiButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/buttons.html')


# /ui/weui/cell
class WeuiCellHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/cell.html')


# /ui/weui/form
class WeuiFormHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/form.html')


# /ui/weui/flex
class WeuiFlexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/flex.html')


# /ui/weui/toast
class WeuiToastHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/toast.html')


# /ui/weui/dialog
class WeuiDialogHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/dialog.html')


# /ui/weui/progress
class WeuiProgressHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/progress.html')


# /ui/weui/msg
class WeuiMsgHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/msg.html')


# /ui/weui/article
class WeuiArticleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/article.html')


# /ui/weui/action-sheet
class WeuiActionSheetHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/action-sheet.html')


# /ui/weui/icons
class WeuiIconsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/icons.html')


# /ui/weui/panel
class WeuiPanelHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/panel.html')


# /ui/weui/navbar
class WeuiNavbarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/navbar.html')


# /ui/weui/tabbar
class WeuiTabbarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/tabbar.html')


# /ui/weui/searchbar
class WeuiSearchbarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/searchbar.html')


# /ui/weui/toptip
class WeuiToptipHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/toptip.html')


# /ui/weui/loadmore
class WeuiLoadmoreHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/loadmore.html')


# /ui/weui/slider
class WeuiSliderHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/slider.html')


# /ui/weui/uploader
class WeuiUploaderHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/uploader.html')


# /ui/weui/badge
class WeuiBadgeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/badge.html')


# /ui/weui/footer
class WeuiFooterHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/footer.html')


# /ui/weui/preview
class WeuiPreviewHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/preview.html')


# /ui/weui/gallery
class WeuiGalleryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/gallery.html')


# /ui/weui/ptr
class WeuiPtrHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/ptr.html')


# /ui/weui/infinite
class WeuiInfiniteHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/infinite.html')


# /ui/weui/picker
class WeuiPickerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/picker.html')


# /ui/weui/calendar
class WeuiCalendarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/calendar.html')


# /ui/weui/city-picker
class WeuiCityPickerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/city-picker.html')


# /ui/weui/datetime-picker
class WeuiDatetimePickerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/datetime-picker.html')


# /ui/weui/swiper
class WeuiSwiperHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/swiper.html')


# /ui/weui/noti
class WeuiNotiHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/noti.html')


# /ui/weui/select
class WeuiSelectHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/select.html')


# /ui/weui/popup
class WeuiPopupHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/popup.html')


# /ui/weui/photo-browser
class WeuiPhotoBrowserHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('jquery-weui/photo-browser.html')
