# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3

"""This module exports the Gfortran plugin class."""

# Since SublimeLinter is loaded after SublimeFortran, we need to manually import Linter
import sublime, os, sys
try:
    sys.path.append(os.path.join(sublime.packages_path(), 'SublimeLinter'))
    from SublimeLinter.lint import Linter
    sys.path.remove(os.path.join(sublime.packages_path(), 'SublimeLinter'))
except (ImportError):
    print("SublimeFortran: Failed to load SublimeLinter")
    class Linter(object):
        pass


class GfortranFixedForm(Linter):
    """Provides an interface to gfortran."""
    cmd = 'gfortran -cpp -fsyntax-only -Wall'
    multiline = True

    # Migrated this upward to keep things neat
    on_stderr = True
    tempfile_suffix = "f"
    
    # Adding defaults:selector arg because this is required by SublimeLinter as of July 2019
    defaults = {
        'selector': 'source.fixedform-fortran'
    }
    
    # Commenting out args that are no longer used by SublimeLinter as of July 2019
    # executable = None
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 4.0'

    # Split this into two paths for Windows systems and otherwise
    if (sys.platform == 'win32'):
        # This Regex block is copied from Kailang's Comment in Issue #28
        regex = (
            r'.*:(?P<line>\d+):(?P<col>\d+):'
            # Then we either have a space or (a newline, a newline, some source code,
            # a newline, a col number, a newline)
            r'(?:(\s*.*\s*\d+\s*))'
            # Finally we have (Error|Warning): message to the end of the line
            r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
        )
    else:
        # This Regex block is retained from the previous commit 
        regex = (
            # filename:line:col: is common for multiline and single line warnings
            r'^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):'
            # Then we either have a space or (a newline, a newline, some source code, a newline, a col number, a newline)
            r'(?:\s|$\r?\n^$\r?\n^.*$\r?\n^\s*\d$\r?\n)'
            # Finally we have (Error|Warning): message to the end of the line
            r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
        )

class GfortranModern(Linter):
    """Provides an interface to gfortran."""
    cmd = 'gfortran -cpp -fsyntax-only -Wall'
    multiline = True

    # Migrated this upward to keep things neat
    tempfile_suffix = "f90"
    on_stderr = True

    # Adding defaults:selector arg because this is required by SublimeLinter as of July 2019
    defaults = {
        'selector': 'source.modern-fortran'
    }
    
    # Commenting out args that are no longer used by SublimeLinter as of July 2019
    #executable = None
    #version_args = '--version'
    #version_re = r'(?P<version>\d+\.\d+\.\d+)'
    #version_requirement = '>= 4.0'

    # Split this into two paths for Windows systems and otherwise
    if (sys.platform == 'win32'):
        # This Regex block is copied from Kailang's Comment in Issue #28
        regex = (
            r'.*:(?P<line>\d+):(?P<col>\d+):'
            # Then we either have a space or (a newline, a newline, some source code,
            # a newline, a col number, a newline)
            r'(?:(\s*.*\s*\d+\s*))'
            # Finally we have (Error|Warning): message to the end of the line
            r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
        )
    else:
        # This Regex block is retained from the previous commit 
        regex = (
            # filename:line:col: is common for multiline and single line warnings
            r'^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):'
            # Then we either have a space or (a newline, a newline, some source code, a newline, a col number, a newline)
            r'(?:\s|$\r?\n^$\r?\n^.*$\r?\n^\s*\d$\r?\n)'
            # Finally we have (Error|Warning): message to the end of the line
            r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
        )
    
