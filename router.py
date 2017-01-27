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
from foo.ui import ui_bootstrapmade


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(ui_cn, 'UicnIndexHandler')),

        (r'/uicn', getattr(ui_cn, 'UicnIndexHandler')),
        (r'/uicn/list', getattr(ui_cn, 'UicnListHandler')),
        (r'/uicn/exp', getattr(ui_cn, 'UicnExpHandler')),
        (r'/uicn/book', getattr(ui_cn, 'UicnBookHandler')),
        (r'/uicn/study', getattr(ui_cn, 'UicnStudyHandler')),
        (r'/uicn/game', getattr(ui_cn, 'UicnGameHandler')),
        (r'/uicn/peixun', getattr(ui_cn, 'UicnPeixunHandler')),
        (r'/uicn/topic', getattr(ui_cn, 'UicnTopicHandler')),
        (r'/uicn/online', getattr(ui_cn, 'UicnOnlineHandler')),
        (r'/uicn/zhaopin', getattr(ui_cn, 'UicnZhaopinHandler')),
        # 列表以及内容页
        (r'/uicn/content', getattr(ui_cn, 'UicnContentHandler')),
        (r'/uicn/zhaopin/cont', getattr(ui_cn, 'UicnZhaopinContHandler')),
        # 认证页面
        (r'/uicn/cert', getattr(ui_cn, 'UicnCertHandler')),

        # 注册 登录 找回
        (r'/auth/login', getattr(ui_cn, 'AuthLoginHandler')),
        (r'/auth/getpass', getattr(ui_cn, 'AuthGetpassHandler')),
        (r'/auth/reg', getattr(ui_cn, 'AuthRegHandler')),
        (r'/auth/findpassbymail', getattr(ui_cn, 'AuthFindpassHandler')),
        (r'/auth/changepass', getattr(ui_cn, 'AuthChangepassHandler')),
        (r'/auth/editsuccess', getattr(ui_cn, 'AuthEditsuccessHandler')),
        #  个人中心页
        (r'/uicn/self', getattr(ui_cn, 'UicnSelfHandler')),

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

        (r'/bootstrapmade/one-page', getattr(ui_bootstrapmade, 'BootstrapmadeOnePageHandler')),
        (r'/bootstrapmade/butterfly', getattr(ui_bootstrapmade, 'BootstrapmadeButterflyHandler')),
        (r'/bootstrapmade/coming-soon', getattr(ui_bootstrapmade, 'BootstrapmadeComingSoonHandler')),
        (r'/bootstrapmade/delicious', getattr(ui_bootstrapmade, 'BootstrapmadeDeliciousHandler')),
        (r'/bootstrapmade/knight', getattr(ui_bootstrapmade, 'BootstrapmadeKnightHandler')),
        (r'/bootstrapmade/laura', getattr(ui_bootstrapmade, 'BootstrapmadeLauraHandler')),
        (r'/bootstrapmade/medilab', getattr(ui_bootstrapmade, 'BootstrapmadeMedilabHandler')),
        (r'/bootstrapmade/mentor', getattr(ui_bootstrapmade, 'BootstrapmadeMentorHandler')),
        (r'/bootstrapmade/squad', getattr(ui_bootstrapmade, 'BootstrapmadeSquadHandler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
