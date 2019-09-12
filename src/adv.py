from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mouth beckons",
                    [
                        Item("Sword", "A sword, it's a little rusty"), 
                        Item("Staff", "A staff, basically just a stick")
                    ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Rocks", "Some rocks, nothing special.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Broken Lantern", "It smells of old oil")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Coin", "One side has a face you don't recognize. The other has an eagle.")]),
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
name = input("What is your name? ")
player = Player(name, room['outside'], [])

action = ''

print(f"\n{player.current_room}")

while action is not 'q':
    action = input("Enter an action: ").strip().lower().split(" ")
    if len(action) == 1:
        if action[0] == 'n' or action[0] == 's' or action[0] == 'e' or action[0] == 'w':
            print(player.move(action[0]) + "\n")
        elif action[0] == 'q':
            if input("Are you sure? (y/n) ") != 'y':
                action = ''
                print()
            else:
                action = 'q'
                print()
        elif action[0] == 'inventory':
            player.check_inventory()
        elif action[0] == 'look':
            print(f"\n{player.current_room}")
        else:
            print("Please input a valid action")
    elif len(action) == 2:
        if action[0] == 'get':
            for i in player.current_room.items:
                if i.name.lower().split(" ")[0] == action[1]:
                    player.pickup(i)
                    action = ''
                elif len(action) > 0:
                    print("That item does not exist\n")
        elif action[0] == 'drop':
            for i in player.items:
                if i.name.lower().split(" ")[0] == action[1]:
                    player.drop(i)
                elif len(action) > 0:
                    print("That item does not exist\n")
    else:
        print("Please input a valid action")


print("Thanks for playing")