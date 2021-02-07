#!/usr/bin/env python3
# string_strip.py - it strip() a string

import re


def strip(string, char='def'):

    if char == 'def':  # default whitespace
        regex = re.compile(r'^\s*')
        return regex.sub('', string)

    else:  # using char as strip character
        regex = re.compile(char)
        return regex.sub('', string)


def main():
    string = "---hola---"
    print(strip(string, char='-'))


main()
