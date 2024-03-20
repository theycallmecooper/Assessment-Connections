#CONNECTIONS ASSESSMENT

import random
from colorama import init, Fore, Back, Style

max_guesses = 4
def print_words_from_catagories(word_categories):
    for category in word_categories:
        print(category["Linking_word"])
        print(category["words"])

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
        "Linking_word" : "BBL",
        "words" : ["Renegade", "Striker", "Thunder", "Hurricane"] #5
    }

    nrl_teams = {
        "Linking_word" : "NRL",
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

    sea = {
        "Linking_word" : "Sea",
        "words" : ["Lion", "Serpent", "Eagle", "Urchin"] #10
    }

    green = {
        "Linking_word" : "Green",
        "words" : ["Grocer", "Machine", "House", "Screen"] #11
    }

    peninsula = {
        "Linking_word" : "Peninsula",
        "words" : ["Arabian", "Balkan", "Iberian", "Italian"] #12
    }

    #Appending
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
    word_categories.append(sea)
    word_categories.append(green)
    word_categories.append(peninsula)

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

#Shuffles category words
def shuffle_categories(selected_categories):
    random.shuffle(selected_categories)

# Main part of the code begins here.
#word_grid = create_grid()
word_categories = setup_word_categories()

# Function to display the game grid.
def display_game(word_categories, grid_size):
    c = 65 # ASCII value for 'A'.

    # Shuffle the words within each category
    for category in word_categories:
        random.shuffle(category["words"])

     # Randomly select 4 categories for the game.
    selected_categories = random.sample(word_categories, 4)

    # First row
    print(Fore.WHITE + f" ", end=' ') #These lines relate to 1, 2, 3 & 4
    for j in range(grid_size):
        print(Fore.WHITE + f"|  {j+1} ", end='') #this makes the lines between the slots
    print(Fore.WHITE + "|") #this makes the final line between the slots
    print(Fore.WHITE + (grid_size*4 + 21)*"-") #this makes the dotted line thing that makes it look neat

    # Other rows
    for i in range(grid_size): #These lines relate to rows A - D
        print(Fore.WHITE + f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            # Access the shuffled words within each category
            word = selected_categories[i]['words'][j]
            print(Fore.WHITE + f"| {word} ", end='') #this makes the lines between the slots
        print(Fore.WHITE + "|") #this makes the final line between the slots
        print(Fore.WHITE + (grid_size*4 + 21)*"-") #this makes the dotted line thing that makes it look neat

    return selected_categories

# Function to let the player guess the linking words.
def guess_linking_word(selected_categories):
    max_guesses = 4  # max guesses
    correct_guesses = 0  # Initialise the number of correct guesses
    guesses = 0  # the initial number of guesses

    while guesses < max_guesses:
        guess_words = input(Fore.YELLOW + "Guess 4 connected words from any category separated by commas: ").split(',')

        found_category = False
        for category in selected_categories:
            if set(guess_words) <= set(category['words']):  # Check if guessed words are a subset of category words
                found_category = True
                guess = input(Fore.GREEN + f"Guess the linking word for the category {category['Linking_word']}: ")
                if guess.lower() == category['Linking_word'].lower():
                    print(Fore.GREEN + "Correct! You connected!")
                    correct_guesses += 1
                    if correct_guesses == len(selected_categories):
                        print(Fore.GREEN + "Congratulations! You guessed all linking words correctly. YOU WIN!")
                        return True
                    else:
                        print(f"You've connected {correct_guesses} out of {len(selected_categories)} categories.")
                    break
                else:
                    print(Fore.RED + "Incorrect guess!")
                    guesses += 1
                    remaining_guesses = max_guesses - guesses
                    print(Fore.MAGENTA + f"You have {remaining_guesses} guesses remaining.")
                    break

        if not found_category:
            print(Fore.RED + "Words entered don't belong to any category!")
            guesses += 1

    print(Fore.RED + "You ran out of guesses. YOU LOSE! ---- The correct linking words were:")
    for category in selected_categories:
        print(f"{category['Linking_word']} - {', '.join(category['words'])}")

    return False

# Set up word categories and select 4 random categories for the game.
word_categories = setup_word_categories()
selected_categories = random.sample(word_categories, 4)

# Display the game grid and let the player guess the linking words.
selected_categories = display_game(word_categories, 4)
guess_linking_word(selected_categories)
#print_words_from_catagories(word_categories)      #prints words from each category in a list