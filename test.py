commands = {
    'N': 'North', 'S': 'South', 'E': 'East', 'W': 'West', 'G': 'Get'
}
player_command = input("Enter your command:\n")
print(commands[player_command[0].upper()])
