#!/usr/bin/env python3

def display_inventory(inventory):
    """Prints an inventory"""
    print('Inventory:')
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
    print(f'Total items: {sum(inventory.values())}')


if __name__ == '__main__':
    my_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(my_inventory)
