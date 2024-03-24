#HARD DICTIONARIES

def hard_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    water = {
        "Linking_word" : "Water",
        "words" : ["Water", "H2O", "Aqua", "Adam's Ale"] #1
    }

    hand_digits = {
        "Linking_word" : "Hand Digits",
        "words" : ["Index", "Middle", "Thumb", "Pinky"] #3
    }

    bbl_teams = {
        "Linking_word" : "BBL",
        "words" : ["Renegade", "Striker", "Thunder", "Hurricane"] #5
    }

    paleozoic = {
        "Linking_word" : "Paleozoic",
        "words" : ["Permian", "Ordocician", "Devonian", "Cambrian"] #7
    }

    tertiary = {
        "Linking_word" : "Tertiary",
        "words" : ["Eocene", "Oligocene", "Miocene", "Pliocene"] #8
    }

    peninsula = {
        "Linking_word" : "Peninsula",
        "words" : ["Arabian", "Balkan", "Iberian", "Italian"] #12
    }

    #Appending
    word_categories.append(water)
    word_categories.append(hand_digits)
    word_categories.append(bbl_teams)
    word_categories.append(paleozoic)
    word_categories.append(tertiary)
    word_categories.append(peninsula)

    return word_categories