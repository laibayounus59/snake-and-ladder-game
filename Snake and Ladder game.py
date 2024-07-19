import random
snakes = {16: 6, 46: 26, 49: 11, 56: 50, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {2: 36, 7: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
def print_board(player1, player2):
    print(f"Player 1 is at position {player_1}")
    print(f"Player 2 is at position {player_2}")
def check_Snakes_ladders(position):
    if position in snakes:
        print(f"Oh, snake bite you! You go from {position} to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"hurrah, You climb the ladder! You go from {position} to {ladders[position]}")
        return ladders[position]
    else:
        return position
def roll_dice():
    return random.randint(1, 6)
def snake_and_ladder():
    player_1, player_2 = 0, 0
    turn = 0
    while player_1 < 100 and player_2 < 100:
        Turn += 1
        print(f"Turn {Turn}")
        # Player 1's turn
        input("Player 1: Press Enter to roll the dice")
        Dice = Roll_Dice()
        print(f"Player 1 rolled a {dice}")
        player_1 += Dice
        player_1 = check_snakes_ladders(player_1)
        print_board(player_1, player_2)
        if player_1 >= 100:
            print("Player 1 wins!")
            break
        # Player 2's turn
        input("Player 2: Press Enter to roll the dice")
        Dice = Roll_Dice()
        print(f"Player 2 rolled a {Dice}")
        player_2 += Dice
        player_2 = check_snakes_ladders(player_2)
        print_board(player_1, player_2)
        if player_2 >= 100:
            print("Player 2 wins!")
            break
Snake_and_ladder()

