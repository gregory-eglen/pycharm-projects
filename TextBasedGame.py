# TextBasedGame.py
# Written by: Gregory Eglen
# 06/19/2021

# Initialize Player Location
player_location = 'City Park'

# Initialize Player Inventory
player_inventory = []

# Initialize input validator
input_validation = 0

# This is a dictionary containing the areas of the game and how they connect to each other
area_map = {
    'City Park': {'North': 'Ruined Hospital', 'East': 'Your Old Home', 'South': 'Collapsed Archway',
                  'West': 'Crumbled School'},
    'Your Old Home': {'North': 'Nikola, Co.', 'West': 'City Park'},
    'Crumbled School': {'North': 'Abandoned Police Station', 'East': 'City Park'},
    'Abandoned Police Station': {'East': 'Ruined Hospital', 'South': 'Crumbled School'},
    'Ruined Hospital': {'East': 'Nikola, Co.', 'South': 'City Park', 'West': 'Abandoned Police Station'},
    'Nikola, Co.': {'North': 'Ruined Lab', 'South': 'Your Old Home', 'West': 'Ruined Hospital'},
    'Ruined Lab': {'South': 'Nikola, Co.'},
    'Collapsed Archway': 'There is no escape.'
}

# This is a dictionary containing the descriptions of the room
area_descriptions = {
    'City Park': {
        'Description': 'The City Park was once a beautiful place. An immaculately maintained green space\n'
                       'The whole family could enjoy. Now all that remains are charred corpses and overgrown vines.\n'
                       'The only way to leave the city is to the South, but a creature blocks the Collapsed Archway.',
        'Item': 'Nothing'},
    'Ruined Hospital': {
        'Description': "The city's hospital. The creaking of rusted steel creates a audible nightmare. ",
        'Item': 'Head and Body'},
    'Collapsed Archway': {
        'Description': "The collapsed archway is your only escape from the city. A gigantic creature blocks the\n"
                       "narrow pathway leading to freedom. Hopefully you are ready.\n",
        'Item': 'Nothing'},
    'Crumbled School': {
        'Description': 'Your childhood school. You remember kissing your first crush under the bleachers.\n'
                       'Now the only thing you see is a pile of corpses crushed under the bleachers.\n',
        'Item': 'Left Arm'},
    'Abandoned Police Station': {
        'Description': "The city's police used to hold off the toxic creatures. As the fiends multiplied\n"
                       "eventually even the bravest among them escaped the city while they still could\n",
        'Item': 'Left Leg'},
    'Your Old Home': {
        'Description': 'Your house. Or, it used to be. You try to think about anything else right now.',
        'Item': 'Right Leg'},
    'Nikola, Co.': {
        'Description': 'At the height of civilization, the scientists were worshipped as saviors\n'
                       'as the source of the creatures became apparent, they became sacrifices.',
        'Item': 'Right Arm'},
    'Ruined Lab': {
        'Description': 'The smell... This is the top secret lab of Nikola, Co. Who knows what horrors occurred here',
        'Item': 'Nega-Sword'}
}

# A dictionary to convert player commands into what the code is looking for
commands = {
    'N': 'North', 'S': 'South', 'E': 'East', 'W': 'West', 'G': 'Get'
}


def title_card():
    # This function displays the title card and the name of our studio
    print("##############################")
    print("# Escape From Nightmare City #")
    print("##############################")
    print("\n")
    print("From G-Funk Studios")
    print("\n")


def game_introduction():
    # This function displays the introduction to the scenario
    print("""The year is 3031. Corporations have been deregulated to the point
of unchecked contamination of the environment. The toxic sewage expelled 
from the bowels of these temples of unchecked greed has created nightmarish 
mutations in the wildlife that roam these tainted lands. You have relied 
on your faithful robot companion, R-66Y, to keep you safe from these 
creatures while traveling the post-apocalyptic hell-scape you used to 
call home. One night, you are ambushed by a particularly nasty beast, 
and R-66Y has been destroyed. You manage to hide yourself during the battle, 
but now this nightmare creature blocks the only exit from the city ruins. 
You must gather the pieces of you fallen companion and locate a weapon 
capable of taking down your would-be reaper. You have heard 
that Nikola, Co. was developing an anti-matter weapon before the fall. 
This fabled weapon is now your only hope to...
 
Escape From Nightmare City! 
""")


def show_inventory():
    # This function shows the player the items in their inventory
    if len(player_inventory) == 0:
        print('')
        print('You have nothing.')
        print('')
    else:
        print('')
        for item in player_inventory:
            print(item, '\n')
        print('')


def print_instructions():
    # This function shows the available inputs a player can use
    print('')
    print('You can type N, S, E, or W to move in a cardinal direction.')
    print('L to look around. G to get item. I to check your inventory')
    print('')


def pickup_item(current_room):
    # This function checks if an item is in the room, and adds it to the player's inventory
    if area_descriptions[current_room]['Item'] != 'Nothing':
        print('')
        print('You pickup {}'.format(area_descriptions[current_room]['Item']))
        print('')
        player_inventory.append(area_descriptions[current_room]['Item'])
        area_descriptions[current_room]['Item'] = 'Nothing'
    else:
        print('There is nothing here.')


def move_player(current_room, player_input):
    # This function contains the areas of the game and the proper way to handle movement between them
    if player_input in area_map[current_room]:
        global player_location
        global input_validation
        print('')
        print('You move {} toward {}.'.format(player_input, area_map[current_room][player_input]))
        player_location = area_map[current_room][player_input]
        input_validation = 1
    else:
        print('You can not go this way.')


def room_description(current_room):
    # This function gives the player a description of the current room,
    # the item in the room, and the locations they can travel to
    print('')
    print(area_descriptions[current_room]['Description'])
    print('')
    if area_descriptions[current_room]['Item'] != 'Nothing':
        print('You see {}.'.format(area_descriptions[current_room]['Item']))
        print('')
    if current_room == 'Collapsed Archway':
        print(area_map[current_room])
    else:
        for direction in area_map[current_room]:
            print('To the {} you can see {}'.format(direction, area_map[current_room][direction]))
    print('')


def game_over():
    # This function prints the game over screen for the player. Also says how close they were to completion
    print("You approach the creature. You do not have your robotic companion completed yet. As you prepare to")
    print("defend yourself, the creature pounces. You don't stand a chance.")
    print("")
    print("Game Over")
    print("You collected {} out of 6 items required to defeat the Nightmare Creature.".format(len(player_inventory)))
    input('Press ENTER to exit the game')


def player_win():
    # This function prints the win screen for the player
    print('As you approach the archway, the pieces of your robotic friend start to vibrate in your satchel.')
    print('The energy from the Nega-Sword you acquired from the Ruined Lab of Nikola, Co. is causing a reaction.')
    print('The parts of R-66Y suddenly fuse together, the glowing sword brandished in his right hand.')
    print('As the creature pounces, R-66Y cuts the foul beast in twain with a single swipe.')
    print('You are free to leave Nightmare City now. Where will your adventures take you next?')
    print('')
    print('Congratulations! A winner is you!!!')
    input('Press ENTER to exit the game')


def main():
    # This Function contains the main gameplay loop
    global input_validation
    title_card()
    game_introduction()
    while player_location != 'Collapsed Archway':
        # This loop keeps repeating until the player enters the boss room, the Collapsed Archway
        print('')
        print('You are at {}'.format(player_location))
        print('')
        input_validation = 0
        while input_validation != 1:
            # This loop continues until the player enters a valid command for moving or getting an item.
            player_input = input('What will you do? (Type "H" for commands)\n')
            if player_input[0].upper() in ('N', 'S', 'E', 'W'):
                move_player(player_location, commands[player_input[0].upper()])
                input_validation = 1
            elif player_input[0].upper() == 'G':
                pickup_item(player_location)
                input_validation = 1
            elif player_input[0].upper() == 'L':
                room_description(player_location)
            elif player_input[0].upper() == 'H':
                print_instructions()
            elif player_input[0].upper() == 'I':
                show_inventory()
            else:
                print('Invalid command')

    room_description(player_location)

    # This statement checks if the player has collected all of the required items to win the game
    if len(player_inventory) >= 6:
        player_win()
    else:
        game_over()


main()
