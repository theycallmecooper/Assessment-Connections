## Fong Categories ##

def fong_word_categories():
    word_categories = []

    premier_league = {
        "Linking_word" : "Premier League Teams",
        "words" : ["bournemouth", "brentford", "brighton", "burnley"]
    }

    tutorgroup_not_in_ist = {
        "Linking_word" : "Tutor members not in IST",
        "words" : ["zak", "oli", "jackson", "liam"]
    }

    recently_left_hutcho_staff = {
        "Linking_word" : "Hutcho staff that left",
        "words" : ["mokwa", "bignold", "macken", "woolley"]
    }

    yr10_game_bands = {
        "Linking_word" : "Bands featured in Cooper's Yr 10 game",
        "words" : ["abba", "dire straits", "carpenters", "verve"]
    }

    brown_eyes = {
        "Linking_word" : "Brown Eyes",
        "words" : ["oliver", "chris", "jaden", "nick"]
    }

    names_in_gaelic = {
        "Linking_word" : "Gaelic Names",
        "words" : ["anndra", "eubh", "daidh", "dughlas"]
    }

    blue_eyes = {
        "Linking_word" : "Blue Eyes",
        "words" : ["joshua", "lucas", "harrison", "zac"]
    }

    nicknames = {
        "Linking_word" : "Class Nicknames",
        "words" : ["fisher", "boss", "spinny", "d-mass"]
    }

    chris_pencilcase = {
        "Linking_word" : "Objects in Chris' Pencilcase",
        "words" : ["casio", "piss pen", "uhu stic", "stabilo"]
    }


    #Appending
    word_categories.append(premier_league)
    word_categories.append(tutorgroup_not_in_ist)
    word_categories.append(recently_left_hutcho_staff)
    word_categories.append(yr10_game_bands)
    word_categories.append(brown_eyes)
    word_categories.append(names_in_gaelic)
    word_categories.append(blue_eyes)
    word_categories.append(nicknames)
    word_categories.append(chris_pencilcase)



    return word_categories