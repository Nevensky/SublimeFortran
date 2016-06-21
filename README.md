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

## Disabling rulers ##

The Fixed Form Fortran syntax included in this package sets some rulers to help code indentation and show where the 72 character limit is. If you find these distracting, they can be disabled by creating a language specific settings file.

To do this, create a file called `FortranFixedForm.sublime-settings` in your `Packages/User/` containing the following:
```JSON
{
    "rulers": []
}
```




## Using the linter ##

This package includes a linter based on SublimeLinter3. SublimeLinter user settings can be modified by selecting `SublimeLinter Settings - User` from the Command Palette.

You may need to tell SublimeLinter where `gfortran` is located by adding it to `paths` in SublimeLinter user settings:

```JSON
{
    "user": {
        "paths": {
            "linux": [],
            "osx": [
                "/usr/local/bin"
            ],
            "windows": []
        },
    }
}
```
Additional command line flags for `gfortran` may be also specified:
```JSON
{
    "user": {
        "linters": {
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
        },
    }
}
```
The default flags included are currently `-cpp -fsyntax-only -Wall`.
