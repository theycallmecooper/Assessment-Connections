#HARD DICTIONARIES

def hard_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    water = {
        "Linking_word" : "Water",
        "words" : ["water", "h2o", "aqua", "adams ale"] 
    }

    hand_digits = {
        "Linking_word" : "Hand Digits",
        "words" : ["index", "middle", "thumb", "pinky"] 
    }

    bbl_teams = {
        "Linking_word" : "BBL",
        "words" : ["renegade", "striker", "thunder", "hurricane"]
    }

    paleozoic = {
        "Linking_word" : "Paleozoic",
        "words" : ["permian", "ordocician", "devonian", "cambrian"]
    }

    tertiary = {
        "Linking_word" : "Tertiary",
        "words" : ["eocene", "oligocene", "miocene", "pliocene"]
    }

    peninsula = {
        "Linking_word" : "Peninsula",
        "words" : ["arabian", "balkan", "iberian", "italian"]
    }

    #Appending
    word_categories.append(water)
    word_categories.append(hand_digits)
    word_categories.append(bbl_teams)
    word_categories.append(paleozoic)
    word_categories.append(tertiary)
    word_categories.append(peninsula)

    return word_categories