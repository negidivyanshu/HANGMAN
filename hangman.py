import random

def get_random_word():
    random_words = [
        "python", "hangman", "programming", "challenge", "computer", "keyboard", "software",
        "developer", "database", "algorithm", "variable", "iteration", "function", "condition",
        "interface", "application", "framework", "optimization", "debugging", "version"
    ]
    return random.choice(random_words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    while True:
        # WELCOME USER
        print("Welcome to the Hangman!")

        # MAKE A RANDOM WORD APPEAR
        random_word = get_random_word()
        guessed_letters = set()

        print(f"Your word is {display_word(random_word, guessed_letters)}")
        print("""
        You have 6 lives remaining..
        _________
         |  | 
         |  
         |  
         | 
         |
        ----------""")

        # TAKE USERS GUESS
        lives = 6
        while lives > 0:
            user_input = input("Enter a letter: ")

            if user_input in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(user_input)

            if user_input in random_word:
                print(f"Correct! Your word: {display_word(random_word, guessed_letters)}")
            else:
                lives -= 1
                print(f"Wrong:( You now have {lives} lives remaining.")
                hangman_art = [
                    """
                    _________
                     |  | 
                     |  
                     |  
                     | 
                     |
                    ----------
                    """,
                    """
                    _________
                     |  | 
                     |  O
                     |  
                     |  
                     |
                    ----------
                    """,
                    """
                    _________
                     |  | 
                     |  O
                     |  |
                     |  
                     |
                    ----------
                    """,
                  """
                  _________
                   |  | 
                   |  O
                   | /|
                   |  
                   |
                  ----------
                  """,
                    """
                    _________
                     |  | 
                     |  O
                     | /|\\
                     |  
                     |
                    ----------
                    """,
                  """
                  _________
                   |  | 
                   |  O
                   | /|\\
                   | /
                   |
                  ----------
                  """,
                    """
                    _________
                     |  | 
                     |  O
                     | /|\\
                     | / \\
                     |
                    ----------
                    """
                ]
                print(hangman_art[6 - lives])

            if set(random_word) == guessed_letters:
                print("Congratulations! You guessed the word!")
                break

        if lives == 0:
            print(f"Sorry, you ran out of lives. The correct word was: {random_word}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

# Run the Hangman game
hangman()

