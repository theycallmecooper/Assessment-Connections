# CONNECTIONS ASSESSMENT #

## IMPORTED LIBRARIES ##
import random
from random import shuffle
from colorama import init, Fore, Back, Style
from time import sleep
from easy_dictionary1 import easy_word_categories
from hard_dictionary1 import hard_word_categories
from fong_dictionary1 import fong_word_categories

## FORMATTING STUFF ##

# typewriter effect
def typewriter(words):
        for char in words:
            print(char, end='', flush=True) #Typewriter effect
            sleep(0.058)
        print()

# add gap between cells
def gap():
        print(  
        ""
        )

# print function that can print each word from a category(s)
def print_words_from_catagories(word_categories):
    for category in word_categories:
        print(category["Linking_word"])
        print(category["words"])

# creates a grid
def create_grid():
    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)

    return word_grid

# shuffles category words
def shuffle_categories(selected_categories):
    random.shuffle(selected_categories)

#Displays the grid and the words on said grid
def display_game(word_categories, grid_size):
    c = 65  # ASCII value for 'A'.

    # Shuffle the words within each category
    for category in word_categories:
        random.shuffle(category["words"])

    # Randomly select 4 categories for the game.
    selected_categories = random.sample(word_categories, 4)

    # Calculate the maximum word length
    max_word_length = max(len(word) for category in selected_categories for word in category["words"])
    cell_width = max_word_length + 3  # Adding 3 for extra spacing

    #Display top line
    print("=" * (grid_size * (cell_width + 2) + 5)) 

    # Display rows
    for i, category in enumerate(selected_categories):
        for word in category['words']:
            print(f"| {word:<{cell_width}} ", end='')
        print("|")
        print("=" * (grid_size * (cell_width + 2) + 5)) #Makes the line below the categories longer/shorter 

    return selected_categories

# Function to let the player guess the linking words.
def guess_linking_word(selected_categories, max_guesses):
    correct_guesses = 0  # Initialise the number of correct guesses
    guesses = 0  # the initial number of guesses

    while guesses < max_guesses:
        guess_words = input(Fore.YELLOW + "Guess 4 connected words from any category separated by commas: ").lower().split(',')

        found_category = False
        for category in selected_categories:
            if set(guess_words) <= set(category['words']):  # Check if guessed words are a subset of category words
                found_category = True
                typewriter(Fore.GREEN + f"The link for the category is: {category['Linking_word']}")
                correct_guesses += 1
                print(Fore.BLUE + f"You've connected {correct_guesses} out of {len(selected_categories)} categories.")

        if not found_category:
            print(Fore.RED + "INCORRECT GUESS!!!")
            guesses += 1
            remaining_guesses = max_guesses - guesses
            print(Fore.MAGENTA + f"You have {remaining_guesses} guesses remaining.")
            player_shuffle = input(Fore.BLUE + "You you want to shuffle? (y/n)").lower()
            if player_shuffle == 'y':
                shuffle_categories(word_categories, 4)
                display_game(selected_categories, 4)

        if correct_guesses == len(selected_categories):
            print(Fore.GREEN + Style.BRIGHT + "Congratulations! You guessed all linking words correctly. YOU WIN!")
            if guesses == max_guesses - 1:
                typewriter(Fore.MAGENTA + Style.BRIGHT +"Pheww... That was close!")
            return True
    
    if guesses == max_guesses:
        print(Fore.RED + "You ran out of guesses. YOU LOSE! ---- The correct linking words were:")
        for category in selected_categories:
            print(f"{category['Linking_word']} - {', '.join(category['words'])}")

    return False

## GAME LAUNCH ##

easy_mode = easy_word_categories()  #Easy mode: Easier categories, otherwise classic connections gameplay, 4 guesses
hard_mode = hard_word_categories()  #Hard mode: Harder categories, otherwise classic connections gameplay, 3 guesses
fong_mode = fong_word_categories()  #Extreme mode: Harder categories, no shuffling, have to guess the connection in order to get it right, 3 guesses
                                    #Fong mode: Connections closer related to the life of Andraa
word_categories = ""

typewriter(Style.BRIGHT + Fore.GREEN + "WELCOME " + Style.BRIGHT + Fore.MAGENTA + "TO " + Style.BRIGHT + Fore.YELLOW + "CONNECTIONS")
print("        \U0001F642")
gameMode = input(Style.RESET_ALL + "Select game mode| EASY | HARD | EXTREME |:").lower()
if gameMode == "hard" or gameMode == "extreme":
    word_categories = hard_mode
    max_guesses = 3
    if gameMode == "extreme":
        choice = input("Do you want hard categories or fong categories? | Hard | Fong |").lower()
        if choice == "fong":
            word_categories = fong_mode
    if gameMode == "hard":
        choice = input("Do you want hard categories or fong categories? | Hard | Fong |").lower()
        if choice == "fong":
            word_categories = fong_mode
       
        def guess_linking_word(selected_categories, max_guesses):
            correct_guesses = 0  # nitialize the number of correct guesses
            guesses = 0  # Initialize the number of guesses
            while guesses < max_guesses:
                guess_words = input(Fore.YELLOW + "Guess 4 connected words from any category separated by commas: ").lower().split(',')

                found_category = False
                for category in selected_categories:
                    if set(guess_words) <= set(category['words']):  # Check if guessed words are a subset of category words
                        found_category = True
                        typewriter(Fore.GREEN + f"Guess the link for the category: {', '.join(category['words'])}")
                        guess = input(Fore.GREEN + "Your guess: ").lower()
                        if guess.lower() == category['Linking_word'].lower():
                            print(Fore.GREEN + "Correct! You connected!")
                            correct_guesses += 1
                            if correct_guesses == len(selected_categories):
                                print(Fore.GREEN + "Congratulations! You guessed all linking words correctly. YOU WIN!")
                                if guesses == max_guesses - 1:
                                    typewriter(Fore.MAGENTA + Style.BRIGHT +"Pheww... That was close!")
                                return True
                            else:
                                print(Fore.BLUE + f"You've connected {correct_guesses} out of {len(selected_categories)} categories.")
                            break
                        else:
                            print(Fore.RED + "Incorrect guess!")
                            guesses += 1
                            remaining_guesses = max_guesses - guesses
                            print(Fore.MAGENTA + f"You have {remaining_guesses} guesses remaining.")

                if not found_category:
                    print(Fore.RED + "INCORRECT GUESS!!!")
                    guesses += 1
                    remaining_guesses = max_guesses - guesses
                    print(Fore.MAGENTA + f"You have {remaining_guesses} guesses remaining.")

            if guesses == max_guesses:
                print(Fore.RED + "You ran out of guesses. YOU LOSE! ---- The correct linking words were:")
                for category in selected_categories:
                    print(f"{category['Linking_word']} - {', '.join(category['words'])}")
else:
    word_categories = easy_mode
    max_guesses = 4
    choice = input("Do you want easy categories or fong categories? | Easy | Fong |").lower()
    if choice == "fong":
        word_categories = fong_mode

# select four from the chosen game category
selected_categories = random.sample(word_categories, 4)

# Display the game grid and let the player guess the linking words.
selected_categories = display_game(word_categories, 4)

# Get a player guess
guess_linking_word(selected_categories, max_guesses)