#CONNECTIONS ASSESSMENT

def print_words_from_catagories(word_categories):
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories():

    word_categories = []

    test_category1 = {
        "Linking_word" : "Country/Place Homonyms",
        "words" : ["Grease", "Hungry", "Whales", "Turkey"]
    }

    test_category2 = {
        "Linking_word" : "Water Synonyms",
        "words" : ["Water", "H2O", "Aqua", "Adam's Ale"]
    }

    test_category3 = {
        "Linking_word" : "Smelly",
        "words" : ["Reek", "Stench", "Pongy", "Stink"]
    }

    test_category4 = {
        "Linking_word" : "Hand Digits",
        "words" : ["Index", "Middle", "Thumb", "Pinky"]
    }

    test_category5 = {
        "Linking_word" : "Alcohols",
        "words" : ["Vodka", "Beer", "Rum", "Champagne"]
    }

    test_category6 = {
        "Linking_word" : "BBL Teams",
        "words" : ["Renegade", "Striker", "Thunder", "Hurricane"]
    }

    test_category7 = {
        "Linking_word" : "NRL Teams",
        "words" : ["Knight", "Cowboy", "Panther", "Bulldog"]
    }

    test_category8 = {
        "Linking_word" : "Periods in the Paleozoic Era",
        "words" : ["Permian", "Ordocician", "Devonian", "Cambrian"]
    }

    test_category9 = {
        "Linking_word" : "Epochs in the Tertiary Period",
        "words" : ["Eocene", "Oligocene", "Miocene", "Pliocene"]
    }

    test_category10 = {
        "Linking_word" : "Grains",
        "words" : ["Wheat", "Barley", "Oat", "Rice"]
    }

    word_categories.append(test_category1)
    word_categories.append(test_category2)
    word_categories.append(test_category3)
    word_categories.append(test_category4)
    #word_categories.append(test_category5)
    #word_categories.append(test_category6)
    #word_categories.append(test_category7)
    #word_categories.append(test_category8)
    #word_categories.append(test_category9)
    #word_categories.append(test_category10)


    return word_categories

#def create_grid():
    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)

    return word_grid

#def grid_fill():
#place holder function to later populate the grid
    pass

#word_grid = create_grid()
word_categories = setup_word_categories()

def display_game(word_categories, grid_size):
    c = 65

    # First row
    print(f"  ", end='')
    for j in range(grid_size):
        print(f"| {j+1} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

    # Other rows
    for i in range(grid_size):
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            print(f"| {word_categories} ", end='')
        print("| ")
        print((grid_size*4+19)*"-")


display_game(word_categories[0]["words"][0], 4)

#print_words_from_catagories(word_categories)      #prints words from each category
#kjhdkjfhlkjdsnfljesnflskjdnflkdsnflsdn