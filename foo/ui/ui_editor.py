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


# /ui/editor/3rd-party/bootstrap/grid
class Editor3rdPartyBootstrapGridHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/bootstrap/grid.html')


# /ui/editor/3rd-party/bootstrap/lists
class Editor3rdPartyBootstrapListsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/bootstrap/lists.html')


# /ui/editor/3rd-party/bootstrap/modal
class Editor3rdPartyBootstrapModalHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/bootstrap/modal.html')


# /ui/editor/3rd-party/jquery/mobile
class Editor3rdPartyJqueryMobileHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/jquery/mobile.html')


# /ui/editor/3rd-party/jquery/ui_modal
class Editor3rdPartyJqueryUimodalHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/jquery/ui_modal.html')


# /ui/editor/3rd-party/at_js
class Editor3rdPartyAtJsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/at.js.html')


# /ui/editor/3rd-party/code-mirror
class Editor3rdPartyCodeMirrorHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/code-mirror.html')


# /ui/editor/3rd-party/require_js/index
class Editor3rdPartyRequireIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/require_js/index.html')


# /ui/editor/3rd-party/spell-checker
class Editor3rdPartySpellCheckerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/3rd-party/spell-checker/spell-checker.html')


# /ui/editor/api/init_destroy
class EditorApiInitDestroyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/init_destroy.html')


# /ui/editor/api/get_html
class EditorApiGetHtmlHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/get_html.html')


# /ui/editor/api/insert_html
class EditorApiInsertHtmlHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/insert_html.html')


# /ui/editor/api/selection
class EditorApiSelectionHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/selection.html')


# /ui/editor/api/live_content_preview
class EditorApiLiveContentPreviewHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/live_content_preview.html')


# /ui/editor/api/live_code_preview
class EditorApiLiveCodePreviewHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/api/live_code_preview.html')


# /ui/editor/international/direction_rtl
class EditorInternationalDirectionRtlHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/international/direction_rtl.html')


# /ui/editor/international/language
class EditorInternationalLanguageHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/international/language.html')


# /ui/editor/international/rtl_ltr_buttons
class EditorInternationalRtlLtrButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/international/rtl_ltr_buttons.html')


# /ui/editor/buttons/custom_buttons
class EditorButtonsCustomButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/buttons/custom_buttons.html')


# /ui/editor/buttons/custom_dropdown
class EditorButtonsCustomDropdownHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/buttons/custom_dropdown.html')


# /ui/editor/buttons/external_button
class EditorButtonsExternalButtonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/buttons/external_button.html')


# /ui/editor/buttons/subscript_superscript
class EditorButtonsSubscriptSuperscriptHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/buttons/subscript_superscript.html')


# /ui/editor/events/blur_focus
class EditorEventsBlurFocusHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/events/blur_focus.html')


# /ui/editor/events/content_changed
class EditorEventsContentChangedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/events/content_changed.html')


# /ui/editor/events/drop
class EditorEventsDropHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/events/drop.html')


# /ui/editor/events/image_removed
class EditorEventsImageRemovedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/events/image_removed.html')


# /ui/editor/events/initialized_destroy
class EditorEventsInitializedDestroyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/events/initialized_destroy.html')


# /ui/editor/image/custom_button
class EditorImageCustomButtonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/image/custom_button.html')


# /ui/editor/image/image_styles
class EditorImageImageStylesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/image/image_styles.html')


# /ui/editor/image/default_width
class EditorImageDefaultWidthHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/image/default_width.html')


# /ui/editor/image/insert_base64
class EditorImageInsertBase64Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/image/insert_base64.html')


# /ui/editor/init_inside_iframe/basic
class EditorInitInsideIframeBasicHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/init_inside_iframe/basic.html')


# /ui/editor/init_inside_iframe/inline
class EditorInitInsideIframeInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/init_inside_iframe/inline.html')


# /ui/editor/init_on_click/basic
class EditorInitOnClickBasicHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/init_on_click/basic.html')


# /ui/editor/init_on_click/inline
class EditorInitOnClickInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/init_on_click/inline.html')


# /ui/editor/init_on_click/two_editors
class EditorInitOnClickTwoEditorsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/init_on_click/two_editors.html')


# /ui/editor/initialization/init_on_click
class EditorInitializationInitOnClickHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/init_on_click.html')


# /ui/editor/initialization/init_on_button
class EditorInitializationInitOnButtonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/init_on_button.html')


# /ui/editor/initialization/init_on_link
class EditorInitializationInitOnLinkHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/init_on_link.html')


# /ui/editor/initialization/init_on_image
class EditorInitializationInitOnImageHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/init_on_image.html')


# /ui/editor/initialization/init_on_h1
class EditorInitializationInitOnH1Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/init_on_h1.html')


# /ui/editor/initialization/initialized_event
class EditorInitializationInitializedEventHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/initialized_event.html')


# /ui/editor/initialization/edit_in_popup
class EditorInitializationEditInPopupHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/initialization/edit_in_popup.html')


# /ui/editor/link/link_styles
class EditorLinkLinkStylesHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/link/link_styles.html')


# /ui/editor/link/predefined_links
class EditorLinkPredefinedLinksHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/link/predefined_links.html')


# /ui/editor/link/custom_validation
class EditorLinkCustomValidationHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/link/custom_validation.html')


# /ui/editor/plugins/line_breaker
class EditorPluginsLineBreakerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/plugins/line_breaker.html')


# /ui/editor/plugins/quick_insert
class EditorPluginsQuickInsertHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/plugins/quick_insert.html')


# /ui/editor/plugins/char_counter
class EditorPluginsCharCounterHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/plugins/char_counter.html')


# /ui/editor/plugins/full_screen
class EditorPluginsFullScreenHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/plugins/full_screen.html')


# /ui/editor/popups/colors
class EditorPopupsColorsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popups/colors.html')


# /ui/editor/popups/emoticons
class EditorPopupsEmoticonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popups/emoticons.html')


# /ui/editor/popups/custom
class EditorPopupsCustomHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/popups/custom.html')


# /ui/editor/styling/font_family
class EditorStylingFontFamilyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/font_family.html')


# /ui/editor/styling/inline
class EditorStylingInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/inline.html')


# /ui/editor/styling/paragraph
class EditorStylingParagraphHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/paragraph.html')


# /ui/editor/styling/placeholder
class EditorStylingPlaceholderHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/placeholder.html')


# /ui/editor/styling/height
class EditorStylingHeightHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/height.html')


# /ui/editor/styling/adjustable_height
class EditorStylingAdjustableHeightHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/adjustable_height.html')


# /ui/editor/styling/width
class EditorStylingWidthHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/styling/width.html')


# /ui/editor/themes/dark
class EditorThemesDarkHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/themes/dark.html')


# /ui/editor/themes/gray
class EditorThemesGrayHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/themes/gray.html')


# /ui/editor/themes/red
class EditorThemesRedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/themes/red.html')


# /ui/editor/themes/royal
class EditorThemesRoyalHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/themes/royal.html')


# /ui/editor/table/nested
class EditorTableNestedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/table/nested.html')


# /ui/editor/table/resize
class EditorTableResizeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/table/resize.html')


# /ui/editor/table/insert_helper
class EditorTableInsertHelperHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/table/insert_helper.html')


# /ui/editor/table/style
class EditorTableStyleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/table/style.html')


# /ui/editor/table/cell_style
class EditorTableCellStyleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/table/cell_style.html')


# /ui/editor/toolbar/inline
class EditorToolbarInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/inline.html')


# /ui/editor/toolbar/sticky
class EditorToolbarStickyHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/sticky.html')


# /ui/editor/toolbar/buttons
class EditorToolbarButtonsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/buttons.html')


# /ui/editor/toolbar/external
class EditorToolbarExternalHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/external.html')


# /ui/editor/toolbar/external_inline
class EditorToolbarExternalInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/external_inline.html')


# /ui/editor/toolbar/bottom
class EditorToolbarBottomHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/bottom.html')


# /ui/editor/toolbar/offset
class EditorToolbarOffsetHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/offset.html')


# /ui/editor/toolbar/bottom_offset
class EditorToolbarBottomOffsetHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/bottom_offset.html')


# /ui/editor/toolbar/show_selection
class EditorToolbarShowSelectionHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/show_selection.html')


# /ui/editor/toolbar/inline_selection
class EditorToolbarInlineSelectionHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/toolbar/inline_selection.html')


# /ui/editor/paragraph_modes/enter_br
class EditorParagraphModesEnterBrHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paragraph_modes/enter_br.html')


# /ui/editor/paragraph_modes/enter_div
class EditorParagraphModesEnterDivHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paragraph_modes/enter_div.html')


# /ui/editor/paragraph_modes/enter_p
class EditorParagraphModesEnterpHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paragraph_modes/enter_p.html')


# /ui/editor/misc/scrollable_container
class EditorMiscScrollableContainerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/misc/scrollable_container.html')


# /ui/editor/misc/scrollable_container_inline
class EditormiscScrollableContainerInlineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/misc/scrollable_container_inline.html')


# /ui/editor/typing/tab
class EditorTypingTabHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/typing/tab.html')


# /ui/editor/typing/shortcuts
class EditorTypingShortcutsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/typing/shortcuts.html')


# /ui/editor/typing/keep_format
class EditorTypingKeepFormatHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/typing/keep_format.html')


# /ui/editor/paste/plain
class EditorPastePlainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paste/plain.html')


# /ui/editor/paste/attrs
class EditorPasteAttrsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paste/attrs.html')


# /ui/editor/paste/tags
class EditorPasteTagsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('editor/paste/tags.html')
