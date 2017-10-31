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
from foo.ui import ui_legend
from foo.ui import ui_weui
from foo.ui import ui_editor
from foo.ui import ui_blocks
from foo.ui import ui_gentelella


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(ui_cn, 'UicnIndexHandler')),

        (r'/ui/weui', getattr(ui_weui, 'WeuiIndexHandler')),
        (r'/ui/weui/buttons', getattr(ui_weui, 'WeuiButtonsHandler')),
        (r'/ui/weui/cell', getattr(ui_weui, 'WeuiCellHandler')),
        (r'/ui/weui/form', getattr(ui_weui, 'WeuiFormHandler')),
        (r'/ui/weui/flex', getattr(ui_weui, 'WeuiFlexHandler')),
        (r'/ui/weui/toast', getattr(ui_weui, 'WeuiToastHandler')),
        (r'/ui/weui/dialog', getattr(ui_weui, 'WeuiDialogHandler')),
        (r'/ui/weui/progress', getattr(ui_weui, 'WeuiProgressHandler')),
        (r'/ui/weui/msg', getattr(ui_weui, 'WeuiMsgHandler')),
        (r'/ui/weui/article', getattr(ui_weui, 'WeuiArticleHandler')),
        (r'/ui/weui/action-sheet', getattr(ui_weui, 'WeuiActionSheetHandler')),
        (r'/ui/weui/icons', getattr(ui_weui, 'WeuiIconsHandler')),
        (r'/ui/weui/panel', getattr(ui_weui, 'WeuiPanelHandler')),
        (r'/ui/weui/navbar', getattr(ui_weui, 'WeuiNavbarHandler')),
        (r'/ui/weui/tabbar', getattr(ui_weui, 'WeuiTabbarHandler')),
        (r'/ui/weui/searchbar', getattr(ui_weui, 'WeuiSearchbarHandler')),
        (r'/ui/weui/toptip', getattr(ui_weui, 'WeuiToptipHandler')),
        (r'/ui/weui/loadmore', getattr(ui_weui, 'WeuiLoadmoreHandler')),
        (r'/ui/weui/slider', getattr(ui_weui, 'WeuiSliderHandler')),
        (r'/ui/weui/uploader', getattr(ui_weui, 'WeuiUploaderHandler')),
        (r'/ui/weui/badge', getattr(ui_weui, 'WeuiBadgeHandler')),
        (r'/ui/weui/footer', getattr(ui_weui, 'WeuiFooterHandler')),
        (r'/ui/weui/preview', getattr(ui_weui, 'WeuiPreviewHandler')),
        (r'/ui/weui/gallery', getattr(ui_weui, 'WeuiGalleryHandler')),
        (r'/ui/weui/ptr', getattr(ui_weui, 'WeuiPtrHandler')),
        (r'/ui/weui/infinite', getattr(ui_weui, 'WeuiInfiniteHandler')),
        (r'/ui/weui/picker', getattr(ui_weui, 'WeuiPickerHandler')),
        (r'/ui/weui/calendar', getattr(ui_weui, 'WeuiCalendarHandler')),
        (r'/ui/weui/city-picker', getattr(ui_weui, 'WeuiCityPickerHandler')),
        (r'/ui/weui/datetime-picker', getattr(ui_weui, 'WeuiDatetimePickerHandler')),
        (r'/ui/weui/swiper', getattr(ui_weui, 'WeuiSwiperHandler')),
        (r'/ui/weui/noti', getattr(ui_weui, 'WeuiNotiHandler')),
        (r'/ui/weui/select', getattr(ui_weui, 'WeuiSelectHandler')),
        (r'/ui/weui/popup', getattr(ui_weui, 'WeuiPopupHandler')),
        (r'/ui/weui/photo-browser', getattr(ui_weui, 'WeuiPhotoBrowserHandler')),


        (r'/ui/editor', getattr(ui_editor, 'EditorIndexHandler')),
        (r'/ui/editor/popular/full', getattr(ui_editor, 'EditorPopularFullHandler')),
        (r'/ui/editor/popular/toolbar_inline', getattr(ui_editor, 'EditorPopularToolbarInlineHandler')),
        (r'/ui/editor/popular/two_instances', getattr(ui_editor, 'EditorPopularTwoInstancesHandler')),
        (r'/ui/editor/popular/textarea', getattr(ui_editor, 'EditorPopularTextareaHandler')),
        (r'/ui/editor/popular/full_page', getattr(ui_editor, 'EditorPopularFullPageHandler')),
        (r'/ui/editor/popular/iframe', getattr(ui_editor, 'EditorPopularIframeHandler')),
        (r'/ui/editor/popular/disable_edit', getattr(ui_editor, 'EditorPopularDisableEditHandler')),
        (r'/ui/editor/popular/z_index', getattr(ui_editor, 'EditorPopularZindexHandler')),
        (r'/ui/editor/popular/init_on_click', getattr(ui_editor, 'EditorPopularInitOnClickHandler')),
        (r'/ui/editor/popular/toolbar_buttons', getattr(ui_editor, 'EditorPopularToolbarButtonsHandler')),
        (r'/ui/editor/popular/disable_paragraphs', getattr(ui_editor, 'EditorPopularDisableParagraphsHandler')),
        (r'/ui/editor/3rd-party/aviary/index', getattr(ui_editor, 'Editor3rdPartyAviaryIndexHandler')),


        (r'/ui/blocks', getattr(ui_blocks, 'BlocksIndexHandler')),
        (r'/ui/blocks/call_to_action', getattr(ui_blocks, 'BlocksCallToActionHandler')),
        (r'/ui/blocks/contacts', getattr(ui_blocks, 'BlocksContactsHandler')),
        (r'/ui/blocks/contents', getattr(ui_blocks, 'BlocksContentsHandler')),
        (r'/ui/blocks/features', getattr(ui_blocks, 'BlocksFeaturesHandler')),
        (r'/ui/blocks/footers', getattr(ui_blocks, 'BlocksFootersHandler')),
        (r'/ui/blocks/forms', getattr(ui_blocks, 'BlocksFormsHandler')),
        (r'/ui/blocks/headers', getattr(ui_blocks, 'BlocksHeadersHandler')),
        (r'/ui/blocks/pricings', getattr(ui_blocks, 'BlocksPricingsHandler')),
        (r'/ui/blocks/teams', getattr(ui_blocks, 'BlocksTeamsHandler')),
        (r'/ui/blocks/testimonials', getattr(ui_blocks, 'BlocksTestimonialsHandler')),


        (r'/ui/gentelella', getattr(ui_gentelella, 'GentelellaIndexHandler')),
        (r'/ui/gentelella/index2', getattr(ui_gentelella, 'GentelellaIndex2Handler')),
        (r'/ui/gentelella/index3', getattr(ui_gentelella, 'GentelellaIndex3Handler')),
        (r'/ui/gentelella/form', getattr(ui_gentelella, 'GentelellaFormHandler')),
        (r'/ui/gentelella/form_advanced', getattr(ui_gentelella, 'GentelellaFormAdvancedHandler')),
        (r'/ui/gentelella/form_validation', getattr(ui_gentelella, 'GentelellaFormValidationdHandler')),
        (r'/ui/gentelella/form_wizards', getattr(ui_gentelella, 'GentelellaFormWizardsdHandler')),
        (r'/ui/gentelella/form_upload', getattr(ui_gentelella, 'GentelellaFormUploadHandler')),
        (r'/ui/gentelella/form_buttons', getattr(ui_gentelella, 'GentelellaFormButtonsHandler')),
        (r'/ui/gentelella/general_elements', getattr(ui_gentelella, 'GentelellaGeneralElementsHandler')),
        (r'/ui/gentelella/media_gallery', getattr(ui_gentelella, 'GentelellaMediaGalleryHandler')),
        (r'/ui/gentelella/typography', getattr(ui_gentelella, 'GentelellaTypographyHandler')),
        (r'/ui/gentelella/icons', getattr(ui_gentelella, 'GentelellaIconsHandler')),
        (r'/ui/gentelella/glyphicons', getattr(ui_gentelella, 'GentelellaGlyphiconsHandler')),
        (r'/ui/gentelella/widgets', getattr(ui_gentelella, 'GentelellaWidgetsHandler')),
        (r'/ui/gentelella/invoice', getattr(ui_gentelella, 'GentelellaInvoiceHandler')),
        (r'/ui/gentelella/inbox', getattr(ui_gentelella, 'GentelellaInboxHandler')),
        (r'/ui/gentelella/calendar', getattr(ui_gentelella, 'GentelellaCalendarHandler')),
        (r'/ui/gentelella/tables', getattr(ui_gentelella, 'GentelellaTablesHandler')),
        (r'/ui/gentelella/tables_dynamic', getattr(ui_gentelella, 'GentelellaTablesDynamicHandler')),


        (r'/legend', getattr(ui_legend, 'LegendIndexHandler')),
        (r'/legend/article', getattr(ui_legend, 'LegendArticleHandler')),
        (r'/legend/product', getattr(ui_legend, 'LegendProductHandler')),
        (r'/legend/moment', getattr(ui_legend, 'LegendMomentHandler')),
        (r'/legend/moment/add', getattr(ui_legend, 'LegendAddMomentHandler')),
        (r'/legend/comment/add', getattr(ui_legend, 'LegendAddCommentHandler')),
        (r'/legend/product/place-order', getattr(ui_legend, 'LegendProductPlaceOrderHandler')),
        (r'/legend/product/place-order-success', getattr(ui_legend, 'LegendProductPlaceOrderSuccessHandler')),

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
