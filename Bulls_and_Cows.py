from random import randint
from time import time

sep = "-" * 40


def intro():
    print(f"""Hi there!
{sep}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{sep}""")


def generate_number():
    number = 0
    while len(set(str(number))) != 4:
        number = randint(1000, 9999)
    number = str(number)
    return number


def number_of_bulls_cows(guess, number):
    bulls = sum(1 if i1 == i2 else 0 for i1, i2 in zip(guess, number))
    cows = 0
    for a, b in enumerate(guess):
        if guess[a] != number[a] and b in number:
            cows += 1
    return bulls, cows


def wrong_guess(guess, number):
    if not guess.isnumeric():
        print(f"That's not a number!")
    elif len(guess) != 4:
        print(f"Incorrect length!")
    elif len(set(guess)) != 4:
        print(f"Number has duplicates!")
    elif guess[0] == "0":
        print(f"Incorrect, first number is not null!")
    elif guess.isnumeric():
        bulls, cows = number_of_bulls_cows(guess, number)
        if bulls == 1 and cows == 1:
            print(f"{bulls} bull, {cows} cow")
        elif bulls == 1:
            print(f"{bulls} bull, {cows} cows")
        elif cows == 1:
            print(f"{bulls} bulls, {cows} cow")
        else:
            print(f"{bulls} bulls, {cows} cows")


def main_game():
    intro()
    wins = 0
    played = {}

    while input("Enter 'Y' to start the game, any other key to quit: ") in ["Y", "y"]:
        print(sep)
        number = generate_number()
        # print(number)
        guesses = 0
        start = time()
        while (guess := input("Enter a number: ")) != number:
            guesses += 1
            wrong_guess(guess, number)
            print(sep)
        else:
            guesses += 1
            wins += 1
            end = time()
            elapsed_time = round(end - start, 1)
            played.setdefault(wins, guesses)
            print(f"Correct, you've guessed the number in {guesses} guesses!")
            print(f"It took you {elapsed_time} seconds to finish!")
            print(sep)
        print(f"Games won: {wins}".center(len(sep)))
        print(sep)
        print(f">>> Statistics <<<".center(len(sep)))
        for i in played:
            print(f"Game: {i: <3} | Guesses: {played[i]: <3}".center(len(sep)))
        print(sep)
    print("Game Over. Thank you for playing!")


if __name__ == "__main__":
    main_game()
