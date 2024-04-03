#HARD DICTIONARIES

def hard_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    water = {
        "Linking_word" : "water",
        "words" : ["water", "h2o", "aqua", "adams ale"] 
    }

    hand_digits = {
        "Linking_word" : "hand digits",
        "words" : ["index", "middle", "thumb", "pinky"] 
    }

    bbl_teams = {
        "Linking_word" : "bbl teams",
        "words" : ["renegade", "striker", "thunder", "hurricane"]
    }

    paleozoic = {
        "Linking_word" : "paleozoic",
        "words" : ["permian", "ordocician", "devonian", "cambrian"]
    }

    tertiary = {
        "Linking_word" : "tertiary",
        "words" : ["eocene", "oligocene", "miocene", "pliocene"]
    }

    peninsula = {
        "Linking_word" : "peninsula",
        "words" : ["arabian", "balkan", "iberian", "italian"]
    }

    minor_bodies = {
    "Linking_word": "minor bodies",
    "words": ["dwarf planet", "asteroid", "moon", "comet"]
}
    
    beginnings_states = {
    "Linking_word": "start of state names",
    "words": ["new", "south", "queen", "victor"]
}

    #Appending
    word_categories.append(water)
    word_categories.append(hand_digits)
    word_categories.append(bbl_teams)
    word_categories.append(paleozoic)
    word_categories.append(tertiary)
    word_categories.append(peninsula)
    word_categories.append(minor_bodies)
    word_categories.append(beginnings_states)

    return word_categories