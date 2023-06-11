import json

with open('/home/aline/Documentos/PROJETO_3/SportinBET/dados.json') as f:
    data = json.load(f)

options = data['fixtures'][0]['optionMarkets'][0]['options']
names = [option['name']['value'] for option in options]
print(names)
odd= [option['price']['odds'] for option in options]
print(odd)
data_time = data['fixtures'][1]['startDate']
print(data_time)
sport = data['fixtures'][1]['sport']['name']['value']
league = data['fixtures'][1]['competition']['name']['value']
print(sport)
print(league)
#print(data['fixtures'][0]['optionMarkets'][0]['options']['name']['value'])

#0 resultado da Partida 
#1 Chance dupla   tempo regulamentar
#2 1º equipe a marca tempo regulaentar
#3 Ambas  Marcam tempo regulame
#4 Resultado e Ambas Marcam -
#5 Tg 2,5
#6 tg 1,5 
#7 tg 3,5
#8 tg0,5
#9 tg 4,5
#10 tg 5,5 
#11 tg 6,5
#12 Resultado da partida e total de gols - 