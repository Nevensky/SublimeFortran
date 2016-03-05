# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3

"""This module exports the Gfortran plugin class."""

# Since SublimeLinter is loaded after SublimeFortran, we need to manually import Linter
import sublime, os, sys
sys.path.append(os.path.join(sublime.packages_path(), 'SublimeLinter'))
from SublimeLinter.lint import Linter, util
sys.path.remove(os.path.join(sublime.packages_path(), 'SublimeLinter'))


class GfortranFixedForm(Linter):
    """Provides an interface to gfortran."""
    syntax = 'fortranfixedform'
    cmd = 'gfortran -fsyntax-only'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.0'
    multiline = True
    regex = (
        # filename:line:col: is common for multiline and single line warnings
        r'^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):'
        # Then we either have a space or (a newline, a newline, some source code, a newline, a col number, a newline)
        r'(?:\s|$\r?\n^$\r?\n^.*$\r?\n^\s*\d$\r?\n)'
        # Finally we have (Error|Warning): message to the end of the line
        r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
    )
    tempfile_suffix = "f"

class GfortranModern(Linter):
    """Provides an interface to gfortran."""
    syntax = 'fortranmodern'
    cmd = 'gfortran -fsyntax-only'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.0'
    multiline = True
    regex = (
        # filename:line:col: is common for multiline and single line warnings
        r'^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):'
        # Then we either have a space or (a newline, a newline, some source code, a newline, a col number, a newline)
        r'(?:\s|$\r?\n^$\r?\n^.*$\r?\n^\s*\d$\r?\n)'
        # Finally we have (Error|Warning): message to the end of the line
        r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
    )
    tempfile_suffix = "f90"
