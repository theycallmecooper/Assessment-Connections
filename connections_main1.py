#CONNECTIONS ASSESSMENT

import random
def print_words_from_catagories(word_categories):
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories(): #holds the categories

    word_categories = []

    country_homonyms = {
        "Linking_word" : "Country/Place Homonyms",
        "words" : ["Grease", "Hungry", "Whales", "Turkey"] #0
    }

    water = {
        "Linking_word" : "Water Synonyms",
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
        "Linking_word" : "Periods in the Paleozoic Era",
        "words" : ["Permian", "Ordocician", "Devonian", "Cambrian"] #7
    }

    tertiary = {
        "Linking_word" : "Epochs in the Tertiary Period",
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

    # First row
    print(f" ", end=' ') #These lines relate to 1, 2, 3 & 4
    for j in range(grid_size):
        print(f"|  {j+1} ", end='')
    print("|")
    print((grid_size*4 + 21)*"-")

    # Other rows
    for i in range(grid_size): #These lines relate to rows A - D
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            # Access the shuffled words within each category
            word = word_categories[i]['words'][j]
            print(f"| {word} ", end='')
        print("|")
        print((grid_size*4 + 21)*"-")

# Example usage
display_game(word_categories, 4)

#print_words_from_catagories(word_categories)      #prints words from each category in a list