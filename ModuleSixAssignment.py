# ModuleSixAssignment.py
# Written by: Gregory Eglen
# 06/12/2021

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# This is the introduction text when the user starts the game
print()
print(""""Welcome to the simplified dragon text game. We hope you find everything to be... FUNctional.
Enter a cardinal direction (North, South, East, West) to go that direction. Enter Exit to leave the game.
You are going to start in the Great Hall.""")
print()

# This sets the variable tracking the current room the player is in
current_room = 'Great Hall'

# This while loop runs until the player enters Exit as the command.
# Otherwise, it updates current room with the location th player wished to move to
while current_room != 'exit':
    print('You are in the {}'.format(current_room)) # Prints the player's current room
    print()
    for room in rooms[current_room]: # Prints the rooms the player can move to
        print('To the {} you see the {}.'.format(room, rooms[current_room][room]))
        print()
    player_input = input('Please enter your command. Enter a direction (North, South, East, West) or exit to exit the game.\n')
    if player_input in rooms[current_room]: # If the player enters a valid direction, update the current room
        print()
        print('---------------------------------------------------------------')
        print('You move toward {}.'.format(rooms[current_room][player_input]))
        print('---------------------------------------------------------------')
        print()
        current_room = rooms[current_room][player_input]
    elif player_input == 'exit': # If the player enters 'exit', Print the quit message and end the program
        print()
        print('---------------------------------------------------------------')
        print('Goodbye, Adventurer')
        print('---------------------------------------------------------------')
        print()
        current_room = 'exit'
    else: # If the player inputs anything else, print an error message.
        print()
        print('---------------------------------------------------------------')
        print('Sorry, that was an invalid command.')
        print('---------------------------------------------------------------')
        print()



