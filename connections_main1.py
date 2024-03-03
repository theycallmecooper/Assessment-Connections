#CONNECTIONS ASSESSMENT

import random
from colorama import init, Fore, Back, Style

max_guesses = 4
def print_words_from_catagories(word_categories):
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories(): #holds the categories

    word_categories = [] #the following are the categories that will be in use

    country_homonyms = {
        "Linking_word" : "Country Homonyms",
        "words" : ["Grease", "Hungry", "Whales", "Turkey"] #0
    }

    water = {
        "Linking_word" : "Water",
        "words" : ["Water", "H2O", "Aqua", "Adam's Ale"] #1
    }

    smelly = {
        "Linking_word" : "Smelly",
        "words" : ["Reek", "Stench", "Pongy", "Stink"] #2
    }

    hand_digits = {
        "Linking_word" : "Hand Digits",
        "words" : ["Index", "Middle", "Thumb", "Pinky"] #3
    }

    alcohols = {
        "Linking_word" : "Alcohols",
        "words" : ["Vodka", "Beer", "Rum", "Champagne"] #4
    }

    bbl_teams = {
        "Linking_word" : "BBL Teams",
        "words" : ["Renegade", "Striker", "Thunder", "Hurricane"] #5
    }

    nrl_teams = {
        "Linking_word" : "NRL Teams",
        "words" : ["Knight", "Cowboy", "Panther", "Bulldog"] #6
    }

    paleozoic = {
        "Linking_word" : "Paleozoic",
        "words" : ["Permian", "Ordocician", "Devonian", "Cambrian"] #7
    }

    tertiary = {
        "Linking_word" : "Tertiary",
        "words" : ["Eocene", "Oligocene", "Miocene", "Pliocene"] #8
    }

    grains = {
        "Linking_word" : "Grains",
        "words" : ["Wheat", "Barley", "Oat", "Rice"] #9
    }

    word_categories.append(country_homonyms)
    word_categories.append(water)
    word_categories.append(smelly)
    word_categories.append(hand_digits)
    word_categories.append(alcohols)
    word_categories.append(bbl_teams)
    word_categories.append(nrl_teams)
    word_categories.append(paleozoic)
    word_categories.append(tertiary)
    word_categories.append(grains)

    return word_categories

def create_grid():
    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)

    return word_grid

#word_grid = create_grid()
word_categories = setup_word_categories()

def display_game(word_categories, grid_size):
    c = 65

    # Shuffle the words within each category
    for category in word_categories:
        random.shuffle(category["words"])

    selected_categories = random.sample(word_categories, 4)

    # First row
    print(f" ", end=' ') #These lines relate to 1, 2, 3 & 4
    for j in range(grid_size):
        print(f"|  {j+1} ", end='') #this makes the lines between the slots
    print("|") #this makes the final line between the slots
    print((grid_size*4 + 21)*"-") #this makes the dotted line thing that makes it look neat

    # Other rows
    for i in range(grid_size): #These lines relate to rows A - D
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            # Access the shuffled words within each category
            word = selected_categories[i]['words'][j]
            print(f"| {word} ", end='') #this makes the lines between the slots
        print("|") #this makes the final line between the slots
        print((grid_size*4 + 21)*"-") #this makes the dotted line thing that makes it look neat

    return selected_categories

def guess_linking_word(selected_categories):
    max_guesses = 4  #max guesses
    correct_guesses = 0  # Initialise the number of correct guesses
    guesses = 0  #the initial number of guesses

    while guesses < max_guesses:
        guess = input(Fore.YELLOW + "Guess the linking word for a category: ")

        for category in selected_categories:
            if guess.lower() == category['Linking_word'].lower(): #For a correct guess
                print(Fore.GREEN + "Correct! You connected!")
                correct_guesses += 1

                # Check if the player has guessed all categories correctly
                if correct_guesses == len(selected_categories):
                    print(Fore.GREEN + "Congratulations! You guessed all linking words correctly. YOU WIN!")
                    return True
                else:
                    print(f"You've connected {correct_guesses} out of {len(selected_categories)} categories.")
                break # Exit the loop once a correct guess is made
        
        if correct_guesses < len(selected_categories):
            if guess.lower() != category['Linking_word'].lower():
                print(Fore.RED + "Incorrect. Try again.")  # For incorrect guesses
                guesses += 1
                remaining_guesses = max_guesses - guesses
                print(Fore.MAGENTA + f"You have {remaining_guesses} guesses remaining.")

    print(Fore.RED + "You ran out of guesses. YOU LOSE! ---- The correct linking words were:")
    for category in selected_categories:
        print(f"{category['Linking_word']} - {', '.join(category['words'])}")
        
        return False

selected_categories = display_game(word_categories, 4)# Allow the player to make a guess

guess_linking_word(selected_categories)
#print_words_from_catagories(word_categories)      #prints words from each category in a list