#!/usr/bin/env python3
# regex_search.py - opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.

# Notes:
# - Using 'with' statement for the sake of learning safely file operations
# - Folder is selected by user

import pyinputplus as pyip
from pathlib import Path
import re


def main():
    # Gets user's input
    print('Please, introduce a desired folder. Press . for current directory')
    user_folder = pyip.inputFilepath()

    print('Please, introduce a regular expression:')
    user_regex = re.compile(pyip.inputStr())

    # Opens all .txt files in the folder chosen
    path = Path(user_folder)
    for text_file in path.glob('*.txt'):
        with open(text_file, 'r') as file:
            matched_lines = []
            text_lines = file.readlines()
            for line in text_lines:
                if user_regex.search(line) is not None:
                    matched_lines.append(line)
                    matched_file = file.name
            # Print results
            if matched_lines:
                print('\nThe matched lines are:')
                for line in matched_lines:
                    print(' *  %s' % line, sep='')
                print('Filename:', matched_file)


main()

