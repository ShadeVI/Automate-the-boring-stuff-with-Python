stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

stuff = add_to_inventory(stuff, dragon_loot)

def display_inventory(inventory):
    print('Inventory:')
    total_items = 0
    for item, qty in inventory.items():
        print(str(qty) + ' ' + item)
        total_items += qty
    print("Total number of items: " + str(total_items))

display_inventory(stuff)