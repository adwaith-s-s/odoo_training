# -*- coding: utf-8 -*-
from odoo import models, fields


class ThemeFutureFurniture(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_silon_post_copy(self, mod):
        # self.enable_view('theme_silon.silon_header')
        self.disable_view('website.template_header_default_oe_structure_header_default_1')
        self.enable_view('website.template_header_default_align_center')
        self.enable_header_off_canvas()