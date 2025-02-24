import numpy as np

# TODO [1]: implement the guessing_game function
def guessing_game(max_value:int, *,attempts:int)-> tuple[bool, list[int], int]: # hint: return type is tuple[bool, list[int], int]:
    chosen_int:int = np.random.randint(low=1,high=max_value+1)
    guesses: list[int] = []

    print('HI! welcome to the guessing game')
    print(f'You have {attempts} attempts to guess the number between 1 and {max_value}')

    while attempts > 0:
        try:
            guess:int = int(input('Enter your guess: '))
        except ValueError:
            print('Invalid input, please enter a valid number')
            continue

        if 1>guess or guess>max_value :
            print('Invalid input, please enter a valid number')
            continue



        guesses.append(guess)
        attempts -= 1

        if guess == chosen_int:
            print('Congratulations! You have guessed the correct number')
            return True, guesses, chosen_int
        elif guess < chosen_int:
            print(f'Your guess is too low, you have {attempts} attempts left')
        else:
            print(f'Your guess is too high, you have {attempts} attempts left')

    print(f"Sorry, you have lost the game.")
    return False, guesses, chosen_int
    



# TODO [2]: implement the play_game function
def play_game()-> None:
    max_value:int = 20
    attempts:int = 5
    won, guesses, chosen_int = guessing_game(max_value, attempts=attempts)
    while not won:
        assert chosen_int not in guesses ,"there is a problem"
        replay:str = input('Do you want to play again? (yes/no): ')
        if replay.lower() == 'yes':
            won, guesses, chosen_int = guessing_game(max_value, attempts=attempts)
        elif replay.lower() == 'no':
            return
        else:
            print('Invalid input, please enter yes or no')
    assert chosen_int in guesses, 'The chosen number is not in the list of guesses'
        

            
play_game()
