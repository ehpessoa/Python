# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    """
    Displays inventory via print
    :param inventory: Dictionary of current inventory
    :return: None
    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f"Total number of items: {item_total}")


def add_to_inventory(inventory, loot):
    """
    Adds new inventory to current inventory
    :param inventory: Dictionary of current inventory
    :param loot: List of new items found
    :return: None
    """
    for item in loot:
        inventory[item] = inventory.setdefault(item, 0) + 1


add_to_inventory(stuff, dragonLoot)
display_inventory(stuff)
