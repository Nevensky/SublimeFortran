SublimeFortran
==============

Comprehensive syntax highlighting for Fortran in Sublime Text 3.

Features:

 - Separate syntax definitions for fixed-format and modern Fortran.

 - Based on the new
   [sublime-syntax file format](http://www.sublimetext.com/docs/3/syntax.html)
   and therefore currently requires a recent [beta version](http://www.sublimetext.com/3)
   of Sublime Text 3 (minimum build number 3084).

 - Code snippets

 - Indentation rules

 - Linter based on `gfortran` (requires the package [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) to work)

Pull requests are welcome :)


## Using the linter ##

This package includes a linter based on SublimeLinter3.

You may need to tell SublimeLinter where gfortran is located by adding it you the paths in SublimeLinter:

```
...
"paths": {
    "linux": [],
    "osx": [
        "/usr/local/bin"
    ],
    "windows": []
},
...
```
Extra command line flags to gfortran may be specified in your SublimeLinter user settings file:
```
...
"gfortranfixedform": {
    "@disable": false,
    "args": [
        "-fdefault-real-8",
        "-fdefault-double-8"
    ],
    "excludes": []
},
"gfortranmodern": {
    "@disable": false,
    "args": [
        "-fdefault-real-8",
        "-fdefault-double-8",
        "-ffree-line-length-none"
    ],
    "excludes": []
},
...
```
The default flags included are currently `-cpp -fsyntax-only -Wall`.
