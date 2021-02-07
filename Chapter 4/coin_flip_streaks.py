#!/usr/bin/env python3
# I haven't used functions although it could be highly improved by using two functions:
# 1. Generates tail/heads list
# 2. Gets the numberOfStreaks from the list

import random



if __name__ == '__main__':

    while True:
        try:
            number = int(input('Please enter a big number.\n'))
            break
        except ValueError:
            print('Invalid type. Please, enter an integer.')

    # listHeadsAndTails = []
    numberOfStreaks = 0
    size_list = 100
    howmany_streaks = 10
    for experimentNumber in range(number):
        # Generates a list of 100 heads (0) and tails (1) values
        listHeadsAndTails = []
        for n in range(size_list):
            listHeadsAndTails.append(random.randint(0, 1))
        print(listHeadsAndTails)
        previous = None
        count = 0
        singleStreaks = 0
        for current in listHeadsAndTails:
            if previous is None:
                count = 1
            elif previous == current:
                count += 1
                if count == howmany_streaks:
                    singleStreaks += 1
                    numberOfStreaks += singleStreaks
                    # singleStreaks = numberOfStreaks
                    count = 0
            else:
                count = 1

            previous = current
        print('Number of streaks: ', str(singleStreaks))

    print('Chance of streak: %s%%' % (numberOfStreaks / 100))