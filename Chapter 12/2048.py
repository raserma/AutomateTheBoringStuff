#!/usr/bin/env python3
# 2048.py - it opens the game at https://gabrielecirulli.github.io/2048/ and keeps sending up, right, down,
# and left keystrokes to automatically play the game.

# Hardest part was to find the right selector that changes when you win/lose. I don't know what is the text returned
# from the selector when you win as I just played once and of course I lost :D

# Note: It doesn't work totally as it eventually restarts the game in the middle of the loop.
# Not sure what is going on and why selenium doesn't keep trying over until loop condition is matched.

import random, time
from selenium import webdriver


def main():
    choices = ['Keys.DOWN', 'Keys.UP', 'Keys.LEFT', 'Keys.RIGHT']

    # Open Selenium webdriver
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    elem = browser.find_element_by_css_selector('html')
    game_message = ''
    while game_message != 'Game over!' or game_message != 'You won!':
        choice = elem.send_keys(random.choice(choices))
        print(choice)
        time.sleep(1)
        game_message = browser.find_element_by_css_selector('.game-message > p').text

    if game_message == 'Game over!':
        print('You lost')
    else:
        print('You won')
    print(f"Score: {browser.find_element_by_css_selector('.score-container').text} - "
          f"Best: {browser.find_element_by_css_selector('.best-container').text}")


main()
