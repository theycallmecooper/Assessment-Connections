## Fong Categories ##

def fong_word_categories():
    word_categories = []

    premier_league = {
        "Linking_word" : "premier league teams",
        "words" : ["bournemouth", "brentford", "brighton", "burnley"]
    }

    tutorgroup_not_in_ist = {
        "Linking_word" : "tutor members not in ist",
        "words" : ["zak", "oli", "jackson", "liam"]
    }

    recently_left_hutcho_staff = {
        "Linking_word" : "hutcho staff that left",
        "words" : ["mokwa", "bignold", "macken", "woolley"]
    }

    yr10_game_bands = {
        "Linking_word" : "bands featured in cooper's yr 10 game",
        "words" : ["abba", "dire straits", "carpenters", "verve"]
    }

    brown_eyes = {
        "Linking_word" : "brown eyes",
        "words" : ["oliver", "chris", "jaden", "nick"]
    }

    names_in_gaelic = {
        "Linking_word" : "gaelic names",
        "words" : ["anndra", "eubh", "daidh", "dughlas"]
    }

    blue_eyes = {
        "Linking_word" : "blue eyes",
        "words" : ["joshua", "lucas", "harrison", "zac"]
    }

    nicknames = {
        "Linking_word" : "class nicknames",
        "words" : ["fisher", "boss", "spinny", "d-mass"]
    }

    chris_pencilcase = {
        "Linking_word" : "objects in chris' pencilcase",
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