class Item:
    def __init__(self, name, items_description):
        self.name = name
        self.items_description = items_description

    # need to pick up item
    def pick_up(self):
        print(f'\nYou have picked up [{self.name}]')

    # need to drop item
    def drop(self):
        print(f'\nYou have dropped [{self.name}]')

    def __repr__(self):
        return f'{self.name}'

# Declare all the items


items = {
    "sword": Item("sword", "Kills Large Monsters"),
    "dagger": Item("dagger", "Lite Item for Thieving"),
    "torch": Item("torch", "Helps light the way"),
    "chicken": Item("chicken", "Helps build stamina")
}

# link items to room
room['outside'].items = [items['torch']]
room['overlook'].items = [items['dagger'], items['chicken']]
