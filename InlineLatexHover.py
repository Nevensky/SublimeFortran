import sublime
import sublime_plugin

import urllib.parse
import urllib.request
from base64 import b64encode
import plistlib

class InlineLatexHover(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if "Fortran" not in view.settings().get('syntax'):
            return
        if view.settings().get('fortran_disable_latex', False):
            return
        if hover_zone != sublime.HOVER_TEXT:
            return
        scope = view.scope_name(point)
        score = sublime.score_selector(scope, "meta.inline_latex.fortran")
        if score > 0:
            # We are hovering over some embedded latex
            region = InlineLatexHover.extract_inline_latex_scope(view, point)
            latex = view.substr(region)
            # bg, fg = 'ffffff', '222222'
            bg, fg = InlineLatexHover.get_colors(view)

            params = urllib.parse.urlencode({'cht': "tx", 'chl': latex, 'chf': 'bg,s,'+bg, 'chco': fg})
            imgurl = "http://chart.googleapis.com/chart?"+params
            try:
                response = urllib.request.urlopen(imgurl)
                rawdata = response.read()
                imgdata = b64encode(rawdata).decode()
                html_str =  '<img src="data:image/png;base64,%s" />' % imgdata
            except (urllib.error.HTTPError) as e:
                html_str =  '<span class="error">%s<span/>' % str(e)
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

    @staticmethod
    def get_colors(view):
        # Code left here for reference
        # scheme_data is a top level dict for the color scheme
        # It has keys "author", "name", "settings" etc.
        # scheme_data["settings"] contains a list of dicts matching "scope" to "settings".
        # It also has one dict with just "settings", which has non-scope related settings (typically first in list)
        # To get color scheme for a particular scope, find the dict with the scope that matches best.
        scheme_path = view.settings().get("color_scheme")
        scheme_content = sublime.load_binary_resource(scheme_path)
        scheme_data = plistlib.readPlistFromBytes(scheme_content)

        def parse_popupCss(css):
            words = css.split()
            i = 0
            bg = None
            fg = None
            while words[i] != "html":
                i += 1
            while words[i] != "}":
                if words[i] == "background-color:":
                    bg = words[i+1]
                if words[i] == "color:":
                    fg = words[i+1]
                i += 1

            # Defaults if not found
            if bg == None:
                bg = "#FFFFFF"
            if fg == None:
                fg = "#000000"

            # Remove leading # and trailing ;
            bg = bg[1:7]
            fg = fg[1:7]
            return bg, fg

        try:
            # Get colors from popupCss
            css = scheme_data["settings"][0]["settings"]["popupCss"]
            bg, fg = parse_popupCss(css)
        except KeyError:
            try:
                # Get colors from the main section of scheme_data["settings"]
                bg = scheme_data["settings"][0]["settings"]["background"][1:]
                fg = scheme_data["settings"][0]["settings"]["foreground"][1:]
            except KeyError:
                bg = "000000"
                fg = "FFFFFF"

        # # theme_datas contains a list of lists of dicts with theme properties.
        # # Each item in the top-level list represents a resource,
        # # i.e. the original theme file, theme addons, user modifications, etc in resource order
        # # I guess we want the last one? theme_data = theme_datas[-1]
        # # theme_data is a list of dicts with keys:
        # #   "class": "tab_control", "icon_button_control", etc
        # #   "attributes": "right", "dirty", "selected" etc
        # #   "layer3.opacity": 0.75 etc
        # #   "settings": [list of settings that are set to true for this to be applied]
        # theme_filename = sublime.load_settings("Preferences.sublime-settings").get("theme")
        # theme_paths = sublime.find_resources(theme_filename)
        # theme_contents = [sublime.load_resource(x) for x in theme_paths]
        # theme_datas = [sublime.decode_value(x) for x in theme_contents]
        # theme_data = theme_datas[-1]

        return (bg, fg)


