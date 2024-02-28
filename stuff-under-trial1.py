connections = [
    {"Connecting Word": "Country/Place Homonyms", "Words": ["Grease", "Hungry", "Whales", "Turkey"]},
    {"Connecting Word": "Water Synonyms", "Words": ["Water", "H2O", "Aqua", "Adam's Ale"]},
    {"Connecting Word": "Smelly", "Words": ["Reek", "Stench", "Pongy", "Stink"]},
    {"Connecting Word": "Hand Digits", "Words": ["Index", "Middle", "Thumb", "Pinky"]},
    # {"Connecting Word": "Alcohols", "Words": ["Vodka", "Beer", "Rum", "Champagne"]},
    # {"Connecting Word": "BBL Teams", "Words": ["Renegade", "Striker", "Thunder", "Hurricane"]},
    # {"Connecting Word": "NRL Teams", "Words": ["Knight", "Cowboy", "Panther", "Bulldog"]},
    # {"Connecting Word": "Periods in the Paleozoic Era", "Words": ["Permian", "Ordocician", "Devonian", "Cambrian"]},
    # {"Connecting Word": "Epochs in the Tertiary Period", "Words": ["Eocene", "Oligocene", "Miocene", "Pliocene"]},
    # {"Connecting Word": "Grains", "Words": ["Wheat", "Barley", "Oat", "Rice"]},
    # {"Connecting Word": "To Hit", "Words": ["Wallop", "Whale", "Bash", "Hit"]},
]

grid = [
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
]

row = 0
for connection in connections: #for each of the connections, access the dictionary
    col = 0
    for word in connection["Words"]: #within dictionary, get word
        #put the word inside the correct GR
        grid[row][col] = word
        col = col + 1 #moves to the column
    row = row + 1 #moves to next row
print(grid)