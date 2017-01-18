# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web

from foo import comm
from foo.ui import ui_amaze
from foo.ui import ui_cn


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(ui_cn, 'UicnIndexHandler')),

        (r'/uicn', getattr(ui_cn, 'UicnIndexHandler')),

        (r'/amazeui', getattr(ui_amaze, 'AmazeIndexHandler')),
        (r'/amazeui/1', getattr(ui_amaze, 'AmazeIndex1Handler')),
        (r'/amazeui/2', getattr(ui_amaze, 'AmazeIndex2Handler')),
        (r'/amazeui/3', getattr(ui_amaze, 'AmazeIndex3Handler')),
        (r'/amazeui/4', getattr(ui_amaze, 'AmazeIndex4Handler')),
        (r'/amazeui/5', getattr(ui_amaze, 'AmazeIndex5Handler')),
        (r'/amazeui/6', getattr(ui_amaze, 'AmazeIndex6Handler')),
        (r'/amazeui/7', getattr(ui_amaze, 'AmazeIndex7Handler')),
        (r'/amazeui/8', getattr(ui_amaze, 'AmazeIndex8Handler')),
        (r'/amazeui/9', getattr(ui_amaze, 'AmazeIndex9Handler')),
        (r'/amazeui/10', getattr(ui_amaze, 'AmazeIndex10Handler')),
        (r'/amazeui/11', getattr(ui_amaze, 'AmazeIndex11Handler')),
        (r'/amazeui/12', getattr(ui_amaze, 'AmazeIndex12Handler')),
        (r'/amazeui/13', getattr(ui_amaze, 'AmazeIndex13Handler')),
        (r'/amazeui/14', getattr(ui_amaze, 'AmazeIndex14Handler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
