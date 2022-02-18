import json

filename = "./files/user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    "PlayerName" : "Donald Trump",
    "Score" : 345,
    "awards" : ["OR", "NV", "NY"]
}

player2 = {
    "PlayerName": "Hillary Clinton",
    "Score": 346,
    "awards": ["WT", "TX", "MI", "AW"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ------- Save by JSON -----------

json.dump(myplayers, myfile)

myfile.close()

# ------- Load by JSON -----------
myfile = open(filename, mode='r')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award N1: " + str(user['awards'][0]))
    print("Player Award N2: " + str(user['awards'][1]))
    print("Player Award N3: " + str(user['awards'][2]))
    print("-------------------------\n\n")

print("--------------------------\n")

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    for award in user['awards']:
        print("Player Award : " + str(award))

print("-------------------------\n\n")
