Hex Converter
===========================
Author: Björn Carlsson
License: MIT
https://github.com/HackerBaloo/SublimeHexConverter

About
-----
A sublime plugin that converts the selected number to or from decimal
to binary / octal / hexadecimal
It can be done as in place replace of the selected number or the
conversion could be added after the number with a separator

Usage
-----
All you need to do is to press 'ctrl+shift+o' and 
Hex Converter will open the selected file in Total Commander 
or another app if you have changed the  settings

    Hex conversion
        Selection   Result          TypOfConversion
        32          32 / 0x20       Normal
        0x20        0x20 / 32       Normal
        32          0x20            InPlace
        0x20        32              InPlace

    Octal conversion
        Selection   Result          TypOfConversion
        32          32 / 040        Normal
        040         040 / 32        Normal
        32          040             InPlace
        040         32              InPlace

    Binary conversion
        Selection   Result          TypOfConversion
        32          32 / 0b100000   Normal
        0b100000    0b100000 / 32   Normal
        32          0b100000        InPlace
        0b100000    32              InPlace

Configuration
-------------
separator, defaults to ' / '

Installation
------------
**With Package Control:** The easiest way to install Hex Converter is
by using the [Package Control plugin]
(http://wbond.net/sublime_packages/package_control).

**Without Git:** Download the latest source from 
[GitHub](https://github.com/HackerBaloo/SublimeHexConverter) and copy 
the Hex Converter folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone https://github.com/HackerBaloo/SublimeHexConverter

The "Packages" directory can be found in the following locations:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

