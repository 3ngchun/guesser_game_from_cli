import os
import secrets
import sys


def clear_screen(numlines=100):
    """
    Clear the console.
    numlines is an optional argument used only as a fall-back.
    """
    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def to_quit():
    sys.exit(0)


def start_game():
    max_value = input("Please enter the max number to guess to start (Q to quit): ")
    while True:
        if max_value != "q" and max_value != "Q":
            max_value = int(max_value)
            if max_value > 0:
                rand = secrets.randbelow(max_value)
                print(f"The max value for this round is {max_value}")
                break
            else:
                max_value = input("Please input a positive number for your max number (Q to quit): ")
        else:
            to_quit()
    raw_answer = input("Please enter the numeric win condition (Q to quit): ")
    while True:
        if raw_answer != 'q' and raw_answer != 'Q':
            raw_answer = int(raw_answer)
            if raw_answer > 0:
                if raw_answer <= max_value:
                    answer = raw_answer
                    break
                else:
                    raw_answer = input(f"Your win condition cannot be more than {max_value}: ")
            else:
                raw_answer = input(f"Please input a positive number for your win condition (Q to quit): ")
        else:
            to_quit()
    return rand, answer, max_value


def guesser_game():
    rand, answer, max_value = start_game()
    min = 0
    clear_screen()
    print(f"Game start!")
    guess_value = input(f"What is your guess dear? Range {min} to {max_value}! (Q to quit): ")
    while True:
        if guess_value != "q" and guess_value != "Q":
            guess_value = int(guess_value)
            if guess_value > min:
                clear_screen()
                if guess_value == answer:
                    print(answer)
                    to_restart = input("You won! \nTo restart, enter following inside the bracket "
                                       "(Y to cont, anything else to quit): ")
                    if to_restart.lower() == "y":
                        rand, answer, max_value = start_game()
                    else:
                        clear_screen()
                        print("Thanks for playing!")
                        break
                elif guess_value > max_value:
                    print(f"More than your current game max value liao ah. {min} to {max_value} (Q to quit)!")
                else:
                    if guess_value < answer:
                        min = guess_value
                        print(f"Too small le, guess again. {min} to {max_value} (Q to quit): ")
                    else:
                        max_value = guess_value
                        print(f"Too big enough liao lah, guess again. {min} to {max_value} (Q to quit): ")
                guess_value = input(f"Lai guess again. {min} to {max_value} (Q to quit): ")
            else:
                clear_screen()
                guess_value = input(f"Guess a higher number lah bodoh. {min} to {max_value} (Q to quit): ")
        else:
            to_quit()
    to_quit()


def main():
    while True:
        try:
            guesser_game()
        except ValueError:
            clear_screen()
            print("dun play play ah, anyhow typo (restart game as punishment for you)")
            main()


if __name__ == "__main__":
    main()
