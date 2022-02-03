from time import time
from random import choice

sep = "-" * 40


def intro():
    print(f"""Welcome to Tic Tac Toe!
{sep}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid using numbers 1 - 9. 
The WINNER is who succeeds in placing
three of their marks in a:
* horizontal,
* vertical or
* diagonal row
{sep}
Let's start the game!
{sep}""")


def print_desk(desk):
    print('+---+---+---+')
    print(f"| {desk['7']} | {desk['8']} | {desk['9']} |")
    print('+---+---+---+')
    print(f"| {desk['4']} | {desk['5']} | {desk['6']} |")
    print('+---+---+---+')
    print(f"| {desk['1']} | {desk['2']} | {desk['3']} |")
    print('+---+---+---+')


def switch_players(player):
    return 'O' if player == 'X' else 'X'


def winning_conditions(desk):
    if desk['1'] == desk['2'] == desk['3'] != " ":
        print(f"Congratulations, player {desk['1']} won!")
        return True
    elif desk['4'] == desk['5'] == desk['6'] != " ":
        print(f"Congratulations, player {desk['4']} won!")
        return True
    elif desk['7'] == desk['8'] == desk['9'] != " ":
        print(f"Congratulations, player {desk['7']} won!")
        return True
    elif desk['1'] == desk['4'] == desk['7'] != " ":
        print(f"Congratulations, player {desk['1']} won!")
        return True
    elif desk['2'] == desk['5'] == desk['8'] != " ":
        print(f"Congratulations, player {desk['2']} won!")
        return True
    elif desk['3'] == desk['6'] == desk['9'] != " ":
        print(f"Congratulations, player {desk['3']} won!")
        return True
    elif desk['1'] == desk['5'] == desk['9'] != " ":
        print(f"Congratulations, player {desk['1']} won!")
        return True
    elif desk['3'] == desk['5'] == desk['7'] != " ":
        print(f"Congratulations, player {desk['3']} won!")
        return True


def wrong_entry(entry, desk):
    if not entry.isnumeric():
        print(f"That's not a number!")
        return True
    elif int(entry) < 1 or int(entry) > 9:
        print(f"Number is out of range!")
        return True
    elif desk[entry] != " ":
        print("Number has already been selected, choose another one!")
        return True


def reset_desk_to_default(desk):
    for key, value in desk.items():
        if value != " ":
            desk[key] = " "


def restart_game(desk, played):
    restart = input(
        "Enter 'Y' to restart the game or any other key to quit: "
        )
    if restart in ["Y", "y"]:
        print(sep)
        print("Let's play again!")
        print(sep)
        reset_desk_to_default(desk)
        print_desk(desk)
    else:
        print("Game Over. Thank you for playing.")
        print(sep)
        print(f">>> Statistics <<<".center(len(sep)))
        for i in played:
            print(f"Game: {i: <2} | Winner: {played[i]: <2}".center(len(sep)))
        quit()


def timer(start, end):
    elapsed_time = round(end - start, 1)
    print(f"This game took {elapsed_time} seconds.")


def main_game():
    game_desk = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}

    intro()
    moves = 0
    games = 0
    played = {}
    player = choice(["X", "O"])
    print_desk(game_desk)
    start = time()

    while True:
        for _ in range(10):
            print(sep)
            move = input(f"Enter your move, player {player}: ")
            print(sep)
            if wrong_entry(move, game_desk):
                continue
            else:
                moves += 1
                game_desk[move] = player
                print_desk(game_desk)
                if winning_conditions(game_desk):
                    moves = 0
                    games += 1
                    end = time()
                    played.setdefault(games, player)
                    timer(start, end)
                    print(sep)
                    restart_game(game_desk, played)
                elif moves == 9:
                    print("It's a draw!")
                    moves = 0
                    games += 1
                    end = time()
                    played.setdefault(games, "Draw")
                    timer(start, end)
                    print(sep)
                    restart_game(game_desk, played)
                break
        player = switch_players(player)


if __name__ == "__main__":
    main_game()
