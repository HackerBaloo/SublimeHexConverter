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
All you need to do select (or have the cursor right after, convinient if you
just wrote the number you want to convert) a number press alt+shift+h and 
Hex Converter will do a normal hex conversion, the other commands are not yet 
bound to any keys to avoid conflicts, but available in as comments in keymaps
and of course in command palette.

    Hex conversion
        Selection   Result          TypOfConversion     Command Palette
        32          32 / 0x20       Normal              Hex Converter: Convert to/from hexadecimal
        0x20        0x20 / 32       Normal              Hex Converter: Convert to/from hexadecimal
        32          0x20            InPlace             Hex Converter: Convert to/from hexadecimal in place
        0x20        32              InPlace             Hex Converter: Convert to/from hexadecimal in place

    Octal conversion
        Selection   Result          TypOfConversion
        32          32 / 040        Normal              Hex Converter: Convert to/from octal
        040         040 / 32        Normal              Hex Converter: Convert to/from octal
        32          040             InPlace             Hex Converter: Convert to/from octal in place
        040         32              InPlace             Hex Converter: Convert to/from octal in place

    Binary conversion
        Selection   Result          TypOfConversion
        32          32 / 0b100000   Normal              Hex Converter: Convert to/from binary
        0b100000    0b100000 / 32   Normal              Hex Converter: Convert to/from binary
        32          0b100000        InPlace             Hex Converter: Convert to/from binary in place
        0b100000    32              InPlace             Hex Converter: Convert to/from binary in place

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

    git clone https://github.com/HackerBaloo/SublimeHexConverter "Hex Converter"

The "Packages" directory can be found in the following locations:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

