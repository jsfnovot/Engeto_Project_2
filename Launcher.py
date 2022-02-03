from Bulls_and_Cows import main_game as bac_game
from Tic_Tac_Toe import main_game as ttt_game


def game_choice():
    print(f"""
{"*" * 20}
Choose the game you want to play.
{"*" * 20}
1) Bulls and Cows
2) Tic Tac Toe
3) Quit launcher
{"*" * 20}        
""")


def main():
    game_choice()
    while True:
        try:
            game = int(input("Enter the number of your game: "))
            if game in range(1, 4):
                if game == 1:
                    print("Enjoy!")
                    print("")
                    bac_game()
                elif game == 2:
                    print("Enjoy!")
                    print("")
                    ttt_game()
                elif game == 3:
                    print("Quitting the launcher.")
                    quit()
        except ValueError:
            print("Wrong choice.")
            continue


if __name__ == "__main__":
    main()
