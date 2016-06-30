import sublime
import sublime_plugin

import urllib.parse
import urllib.request
from base64 import b64encode

class InlineLatexHover(sublime_plugin.EventListener):
    @classmethod
    def is_applicable(cls, settings):
        return settings.get('syntax').contains("Fortran")

    def on_hover(self, view, point, hover_zone):
        if hover_zone == sublime.HOVER_TEXT:
            scope = view.scope_name(point)
            score = sublime.score_selector(scope, "meta.inline_latex.fortran")
            if score > 0:
                # We are hovering over some embedded latex
                region = InlineLatexHover.extract_inline_latex_scope(view, point)
                latex = view.substr(region)
                # todo: get colors from theme popupCss
                bg, fg = 'ffffff', '222222'
                params = urllib.parse.urlencode({'cht': "tx", 'chl': latex, 'chf': 'bg,s,'+bg, 'chco': fg})
                imgurl = "http://chart.googleapis.com/chart?"+params
                with urllib.request.urlopen(imgurl) as response:
                    rawdata = response.read()
                    imgdata = b64encode(rawdata).decode()
                    html_str =  '<img src="data:image/png;base64,%s" />' % imgdata
                    view.show_popup(html_str, sublime.HIDE_ON_MOUSE_MOVE, point)

    @staticmethod
    def extract_inline_latex_scope(view, point):
        """Like extract_scope(), but extracts the extent of meta.inline_latex.fortran."""
        ltxscope = "meta.inline_latex.fortran"
        istart = point
        iend = point
        while istart > 0 and sublime.score_selector(view.scope_name(istart-1), ltxscope) > 0:
            istart = istart - 1
        while iend < view.size() and sublime.score_selector(view.scope_name(iend), ltxscope) > 0:
            iend = iend + 1
        r = sublime.Region(istart, iend)
        if r.size() > 1000:
            r = sublime.Region(point, point)
        return r
