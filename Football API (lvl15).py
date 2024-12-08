# Football API. First time using an API, so a bit of a learning curve but not too complex. As far as I could tell his NBA API didn't exists anymore, or at least I couldn't find it, so here is my replacement.
# To use yourself, go to https://rapidapi.com/heisenbug/api/premier-league-live-scores/pricing to sign up and get the free plan and API key, paste it into the headers dictionary, then off you go.

import http.client, json, os

SITE = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "(API key)",
    'x-rapidapi-host': "free-api-live-football-data.p.rapidapi.com"
}


def getdata(request):
    # Make the API request
    SITE.request("GET", request, headers=headers)
    res = SITE.getresponse()
    data = res.read()
    
    # Decode and parse the JSON data
    datalist = json.loads(data.decode("utf-8"))
    return datalist


def displaydata(datalist, word):
    os.system('cls')
    # Safely access and display relevant data from the dictionary
    if datalist["status"] == "success":
        suggestions = datalist.get("response", {}).get(word, [])
        if suggestions:
            try:
                for suggestion in suggestions:
                    for thing in suggestion:
                        print(f"{thing}: {suggestion[thing]}")
                    print(" \n")

            except:
                for thing in suggestions:
                    print(f"{thing}: {suggestions[thing]}")
                print(" \n")
        else:
            print("No suggestions found.")
    else:
        print("Failed to retrieve data.") 

    cont = ""
    while cont != "y" and cont != "n":
        cont = input("Would you like to go again (y/n)?   ")
    return False if cont == "y" else True


def players(): 
    player = "".join((input("Enter the player to get their info: ").split(' ')))
    request = f"/football-players-search?search={player}"
    players = getdata(request)
    return displaydata(players, "suggestions")


def teams():
    team = "".join((input("Enter the team name to get their info: ").split(' ')))
    request = f"/football-teams-search?search={team}"
    teams = getdata(request)
    return displaydata(teams, "suggestions")


def leagues():
    leagueid = "".join((input("Enter the league ID to get their info: ").split(' ')))
    request = f"/football-get-league-detail?leagueid={leagueid}"
    league = getdata(request)
    return displaydata(league, "leagues")


over = False
while not over:
    os.system('cls')
    choice = input("What would you like to find data about (player, team, league)?   ")

    if choice.lower() == "player":
        over = players()

    elif choice.lower() == "team":
        over = teams()

    elif choice.lower() == "league":
        over = leagues()
