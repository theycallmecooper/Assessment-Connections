#EASY DICTIONARIES

def easy_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    country_homonyms = {
        "Linking_word" : "Country Homonyms",
        "words" : ["grease", "hungry", "whales", "turkey"] #1
    }

    smelly = {
        "Linking_word" : "Smelly",
        "words" : ["reek", "stench", "pong", "stink"]
    }

    alcohols = {
        "Linking_word" : "Alcohols",
        "words" : ["vodka", "beer", "rum", "champagne"]
    }

    nrl_teams = {
        "Linking_word" : "NRL",
        "words" : ["knight", "cowboy", "panther", "bulldog"]
    }

    grains = {
        "Linking_word" : "Grains",
        "words" : ["wheat", "barley", "oat", "rice"]
    }

    sea = {
        "Linking_word" : "Sea",
        "words" : ["lion", "serpent", "eagle", "urchin"] 
    }

    green = {
        "Linking_word" : "Green",
        "words" : ["grocer", "machine", "house", "screen"]
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