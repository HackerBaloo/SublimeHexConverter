import os
import subprocess
import sublime
import sublime_plugin


def get_separator():
    settings = sublime.load_settings("Hex Converter.sublime-settings")
    return settings.get('separator')


def get_word(view, region):
    new_region = view.word(region)
    value = view.substr(new_region)
    if not value:
        new_region = region.begin() - 1
        value = view.substr(view.word(new_region))
    return value, new_region


def convert(edit, view, prefix, base, in_place):
    print('base: ', base, 'prefix: ', prefix, 'in_place: ', in_place)
    selected_regions = view.sel()
    for region in selected_regions:
        value, new_region = get_word(view, region)
        if value.startswith(prefix):
            result = str(int(value, base))
        else:
            if base == 16:
                result = hex(int(value))
            elif base == 8:
                result = oct(int(value))
            elif base == 2:
                result = bin(int(value))
            else:
                sublime.error_message('Base not implemented: ', base)

        print('result: ', result)
        if in_place:
            view.replace(edit, new_region, result)
        else:
            view.replace(edit, new_region, value + ' / ' + result)
    return value, result


class Base(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

    def run(self, edit):
        value, result = convert(edit, self.view, self.prefix, self.base, 'InPlace' in type(self).__name__)
        sublime.status_message(self.status_message + value + "=" + result)


class ConvertToFromHex(Base):
    def __init__(self, view):
        super(ConvertToFromHex, self).__init__(view)
        self.status_message = "Converted to / from hexadecimal: "
        self.prefix = '0x'
        self.base = 16


class ConvertToFromHexInPlace(ConvertToFromHex):
    def __init__(self, view):
        super(ConvertToFromHexInPlace, self).__init__(view)


class ConvertToFromOctal(Base):
    def __init__(self, view):
        super(ConvertToFromOctal, self).__init__(view)
        self.status_message = "Converted to / from octal: "
        self.prefix = '0'
        self.base = 8


class ConvertToFromOctalInPlace(ConvertToFromOctal):
    def __init__(self, view):
        super(ConvertToFromOctalInPlace, self).__init__(view)


class ConvertToFromBinary(Base):
    def __init__(self, view):
        super(ConvertToFromBinary, self).__init__(view)
        self.status_message = "Converted to / from binary: "
        self.prefix = '0b'
        self.base = 2


class ConvertToFromBinaryInPlace(ConvertToFromBinary):
    def __init__(self, view):
        super(ConvertToFromBinaryInPlace, self).__init__(view)
