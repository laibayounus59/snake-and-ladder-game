import random
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
def print_board(p
                layer1, player2):
    print(f"Player 1 is at position {player1}")
    print(f"Player 2 is at position {player2}")
def check_snakes_ladders(position):
    if position in snakes:
        print(f"Oops, snake bite! You go from {position} to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Yay, ladder climb! You go from {position} to {ladders[position]}")
        return ladders[position]
    else:
        return position
def roll_dice():
    return random.randint(1, 6)
def snake_and_ladder():
    player1, player2 = 0, 0
    turn = 0

    while player1 < 100 and player2 < 100:
        turn += 1
        print(f"Turn {turn}")

        # Player 1's turn
        input("Player 1: Press Enter to roll the dice...")
        dice = roll_dice()
        print(f"Player 1 rolled a {dice}")
        player1 += dice
        player1 = check_snakes_ladders(player1)
        print_board(player1, player2)
        if player1 >= 100:
            print("Player 1 wins!")
            break
        # Player 2's turn
        input("Player 2: Press Enter to roll the dice...")
        dice = roll_dice()
        print(f"Player 2 rolled a {dice}")
        player2 += dice
        player2 = check_snakes_ladders(player2)
        print_board(player1, player2)

        if player2 >= 100:
            print("Player 2 wins!")
            break

snake_and_ladder()

