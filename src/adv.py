# which is where the main logic for the game should live
from room import Room
from player import Player
#


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_0 = Player('Sledge', room['outside'])

game_status = True

# Write a loop that:
while game_status:
    direction = input(
        '\nWhat direction would you like to travel? Keys: n, s, e, or w\n')

    try:
        if direction == 'q':
            print('Exiting!\n')
            game_status = False
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
        if direction == 'n' or direction == 'e' or direction == 's' or direction == 'w':
            attrib = f'{direction}_to'
# * Prints the current description (the textwrap module might be useful here).
            if player_0.current_room.__dict__[attrib] == None:
                print(
                    '\nTravel Ban has been initiated on this path. Choose another direction.\n')
# * Prints the current room name
            else:
                player_0.current_room = player_0.current_room.__dict__[
                    attrib]
                print(player_0)

        else:
            print('Invalid input. Please try again.\n')
    except ValueError:
        print('Invalid input.\n')
