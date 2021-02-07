#!/usr/bin/env python3
# strong_password.py - it makes sure a password is strong
# Note: I divided the regex into 4 expressions to give concise feedback to user
# about why password is not strong enough.

import re


def is_password_strong(password):
    """Validates a strong password"""
    # define the password requisites
    min_characters_regex = re.compile(r'\w{8,}')
    lowercase_regex = re.compile(r'[a-z]+')
    uppercase_regex = re.compile(r'[A-Z]+')
    digit_regex = re.compile(r'\d+')
    if min_characters_regex.search(password) is None:
        print('Your password needs at least 8 characters')
        return False
    if lowercase_regex.search(password) is None:
        print('Your password needs at least 1 lowercase')
        return False
    if uppercase_regex.search(password) is None:
        print('Your password needs at least 1 uppercase')
        return False
    if digit_regex.search(password) is None:
        print('Your password needs at least 1 digit')
        return False

    print('Password strong enough!')
    return True


def main():
    password = input('Introduce your secure password:')
    while not is_password_strong(password):
        print('Try again please.')
        password = input('Introduce your secure password:')


main()
