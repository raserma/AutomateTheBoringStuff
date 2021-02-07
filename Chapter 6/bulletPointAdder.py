#!/usr/bin/env python3
# bulletPointAdder.py - Copy a list on your clipboard and get an amazing bullet point list!

import pyperclip

if __name__ == '__main__':
    # copy from clipboard
    string_copied = pyperclip.paste()

    # Add a `*` before each bullet point
    list_copied = string_copied.split('\n')
    for i in range(len(list_copied)):
        list_copied[i] = '* ' + list_copied[i]
    string_modified = '\n'.join(list_copied)
    # paste to clipboard
    pyperclip.copy(string_modified)

    # print it
    print(string_modified)
