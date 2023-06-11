import time
import requests
from bs4 import BeautifulSoup

jogo = {'Date': [], 'Venue': [], 'Coordinates': [], 'homeFormation': [], 'awayFormation': [], 'HomeName': [], 'AwayName': [], 'currentTime': {'Minute': [], 'Second': []
                                                                                                                                              },
        'HomeScores': [], 'AwayScores': [],
        'weatherReport': {"code": [],
                          "condition": [],
                          "temperature": [],
                          "clouds": [],
                          "humidity": [],
                          "pressure": [],
                          "wind": []},
        'league"': [],
        'Probabilities': {
    "AT_over_0_5": [],
    "AT_over_1_5": [],
    "AT_under_0_5": [],
    "AT_under_1_5": [],
    "HT_over_0_5": [],
    "HT_over_1_5": [],
    "HT_under_0_5": [],
    "HT_under_1_5": [],
    "away": [],
    "btts": [],
    "draw": [],
    "home": [],
    "over_0_5": [],
    "over_1_5": [],
    "over_2_5": [],
    "over_3_5": [],
    "under_0_5": [],
    "under_1_5": [],
    "under_2_5": [],
    "under_3_5": []
}}

while True:
    try:

        url = "https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores"
        querystring = {
            "include": "weatherReport,additionalInfo,league,stats,pressureStats,probabilities"}
        payload = ""
        headers = {
            "cookie": "route=94206abd7dc66948dc67e8b90e588983; SRVGROUP=common"}
        time.sleep(2)
        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)
        soup = BeautifulSoup(requests.get(url).content,  'html.parser')
        dic_response = response.json()
        
        for game in dic_response['data']: 
            jogo["Date"].append(game['date'])

            jogo["Venue"].append(game['venue'])
            jogo["Coordinates"].append(game['coordinates'])
            jogo["homeFormation"].append(game['homeFormation'])
            jogo["awayFormation"].append(game['awayFormation'])

            jogo["HomeName"].append(game['homeTeam']['name'])
            jogo["AwayName"].append(game['awayTeam']['name'])

            jogo["currentTime"]["minute"].append(game['currentTime']['minute'])
            jogo["currentTime"]["second"].append(game['currentTime']['second'])

            jogo["league"].append(game['league']['name'])

            jogo["HomeScores"].append(game['scores']['homeTeamScore'])
            jogo["AwayScores"].append(game['score']['awayTeamScore'])
            print(jogo["Date"],jogo["Venue"],jogo["Coordinates"])


    except:
        pass
    

        