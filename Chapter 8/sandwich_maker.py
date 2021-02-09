#!/usr/bin/env python3
# sandwich_maker.py - it validates inputs from user and calculates
# the price of the sandwich

# Note: Using dictionaries to calculate the price of the sandwich

import pyinputplus as pyip


def calculate_price_sandwich(sandwich):
    """Calculates the price of a single sandwich"""

    bread_prices = {'wheat': 2, 'white': 1, 'sourdough': 3}
    protein_prices = {'chicken': 3, 'turkey': 4, 'ham': 2, 'tofu': 3}
    cheese_prices = {'cheddar': 2, 'Swiss': 3, 'mozzarella': 1, 'no': 0}
    veggie_prices = {'yes': 2, 'no': 0}

    total_price = bread_prices[sandwich['bread']] + protein_prices[sandwich['protein']] + \
        cheese_prices[sandwich['cheese']] + veggie_prices[sandwich['veggies']]

    return total_price


def main():
    sandwich = {'bread': '', 'protein': '', 'cheese': '', 'veggies': ''}
    # User's input
    print('What are your sandwiches preferences?\n')
    print('Bread type?')
    sandwich['bread'] = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    print('Protein type?')
    sandwich['protein'] = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    print('Do you want cheese?')
    sandwich['cheese'] = pyip.inputYesNo()
    if sandwich['cheese'] == 'yes':
        print('Cheese type?')
        sandwich['cheese'] = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    print('Do you want veggies?')
    sandwich['veggies'] = pyip.inputYesNo()
    print('How many sandwiches you want?')
    num_sandwiches = pyip.inputInt(min=1)

    print('Your choices are: ')
    for key, value in sandwich.items():
        print('%s: %s' % (key, value), sep=',')
    print('\nNumber of sandwiches:', num_sandwiches)
    print('The total price is: £%s' % (num_sandwiches * calculate_price_sandwich(sandwich)))


main()
