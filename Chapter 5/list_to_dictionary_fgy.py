#!/usr/bin/env python3
# It adds new stuff into an inventory and shows it in readable format.
#   - v2 function removes the need to loop through the dictionary

# NOTE: Used 'list(my_inventory)' to avoid
# error 'RuntimeError: dictionary changed size during iteration'
def add_to_inventory(inventory, added_items):
    """Adds a list into a dictionary"""
    for key in list(inventory):
        for item in added_items:
            if key == item:
                inventory[key] += 1
            else:
                inventory.setdefault(item, 1)

    return my_inventory


def add_to_inventory_v2(inventory, added_items):
    """
    Adds a list into a dictionary v2
    """

    for item in added_items:
        if item not in inventory:
            my_inventory.setdefault(item, 1)
        else:
            my_inventory[item] += 1
    return my_inventory


def display_inventory(inventory):
    """Prints an inventory"""
    print('Inventory:')
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
    print('Total items: ', sum(inventory.values()))


if __name__ == '__main__':
    my_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    my_added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    # my_inventory = add_to_inventory(my_inventory, my_added_items)
    my_inventory = add_to_inventory_v2(my_inventory, my_added_items)
    display_inventory(my_inventory)
