## Fong Categories ##

def fong_word_categories():
    word_categories = []

    premier_league = {
        "Linking_word" : "Premier League Teams",
        "words" : ["Bournemouth", "Brentford", "Brighton", "Burnley"]
    }

    tutorgroup_not_in_ist = {
        "Linking_word" : "Tutor members not in IST",
        "words" : ["Zak", "Oli", "Jackson", "Liam"]
    }

    recently_left_hutcho_staff = {
        "Linking_word" : "Hutcho staff that left",
        "words" : ["Mokwa", "Bignold", "Macken", "Woolley"]
    }

    yr10_game_bands = {
        "Linking_word" : "Bands featured in Yr 10 game",
        "words" : ["ABBA", "Dire Straits", "Carpenters", "Verve"]
    }

    brown_eyes = {
        "Linking_word" : "Brown Eyes",
        "words" : ["Oliver", "Chris", "Jaden", "Nick"]
    }

    names_in_gaelic = {
        "Linking_word" : "Gaelic Names",
        "words" : ["Anndra", "Eubh", "Daidh", "Dughlas"]
    }


    #Appending
    word_categories.append(premier_league)
    word_categories.append(tutorgroup_not_in_ist)
    word_categories.append(recently_left_hutcho_staff)
    word_categories.append(yr10_game_bands)
    word_categories.append(brown_eyes)
    word_categories.append(names_in_gaelic)

    return word_categories