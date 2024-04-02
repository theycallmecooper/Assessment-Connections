#EASY DICTIONARIES

def easy_word_categories(): #holds the categories
    word_categories = [] #the following are the categories that will be in use

    country_homonyms = {
        "Linking_word" : "country homonyms",
        "words" : ["grease", "hungry", "whales", "turkey"] #1
    }

    smelly = {
        "Linking_word" : "smelly",
        "words" : ["reek", "stench", "pong", "stink"]
    }

    alcohols = {
        "Linking_word" : "alcohols",
        "words" : ["vodka", "beer", "rum", "champagne"]
    }

    nrl_teams = {
        "Linking_word" : "nrl teams",
        "words" : ["knight", "cowboy", "panther", "bulldog"]
    }

    grains = {
        "Linking_word" : "grains",
        "words" : ["wheat", "barley", "oat", "rice"]
    }

    sea = {
        "Linking_word" : "sea",
        "words" : ["lion", "serpent", "eagle", "urchin"] 
    }

    green = {
        "Linking_word" : "green",
        "words" : ["grocer", "machine", "house", "screen"]
    }

    tennis = {
        "Linking_word" : "tennis",
        "words" : ["ball", "raquet", "shoes", "net"]
    }

    

    #Appending
    word_categories.append(country_homonyms)
    word_categories.append(smelly)
    word_categories.append(alcohols)
    word_categories.append(nrl_teams)
    word_categories.append(grains)
    word_categories.append(sea)
    word_categories.append(green)
    word_categories.append(tennis)

    return word_categories