#!/usr/bin/env python3
# madlibs.py - it reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

# Note: I am not entirely sure about the logic of this exercise. On the description,
# there is a reference to ADVERB but on the example this is not used.
#   - Is it expecting to loop over through all the special words?

import pyinputplus as pyip
from pathlib import Path
import re


def main():
    # Reads the file
    file = open(Path.cwd() / 'madlibs_file.txt', 'r')
    lines = file.read()
    file.close()

    print('The text is:\n', lines)

    # Swaps the text
    adj_regex = re.compile('ADJECTIVE')
    noun_regex = re.compile(r'NOUN')
    verb_regex = re.compile(r'VERB')
    adv_regex = re.compile(r'ADVERB')

    # Loops through all the special words until there is none
    while adj_regex.search(lines) is not None:
        print('Enter an adjective:')
        lines = adj_regex.sub(pyip.inputStr(), lines, 1)
        print('The text is now:')
        print(lines)
    while noun_regex.search(lines) is not None:
        print('Enter an noun:')
        lines = noun_regex.sub(pyip.inputStr(), lines, 1)
        print('The text is now:')
        print(lines)
    while verb_regex.search(lines) is not None:
        print('Enter an verb:')
        lines = verb_regex.sub(pyip.inputStr(), lines, 1)
        print('The text is now:')
        print(lines)
    while adv_regex.search(lines) is not None:
        print('Enter an adverb:')
        lines = adv_regex.sub(pyip.inputStr(), lines, 1)
        print('The text is now:')
        print(lines)

    # Creates a new file with new text
    new_file = open(Path.cwd() / 'madlibs_file_out.txt', 'w')
    new_file.write(lines)
    new_file.close()


main()
