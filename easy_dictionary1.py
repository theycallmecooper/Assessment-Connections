#EASY DICTIONARIES

def easy_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    country_homonyms = {
        "Linking_word" : "Country Homonyms",
        "words" : ["Grease", "Hungry", "Whales", "Turkey"] #1
    }

    smelly = {
        "Linking_word" : "Smelly",
        "words" : ["Reek", "Stench", "Pong", "Stink"] #2
    }

    alcohols = {
        "Linking_word" : "Alcohols",
        "words" : ["Vodka", "Beer", "Rum", "Champagne"] #4
    }

    nrl_teams = {
        "Linking_word" : "NRL",
        "words" : ["Knight", "Cowboy", "Panther", "Bulldog"] #6
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

    #Appending
    word_categories.append(country_homonyms)
    word_categories.append(smelly)
    word_categories.append(alcohols)
    word_categories.append(nrl_teams)
    word_categories.append(grains)
    word_categories.append(sea)
    word_categories.append(green)

    return word_categories