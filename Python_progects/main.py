import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
body_new_pokemons = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "65900",
    "name": "New Name"
}
body_pokeball={
    "pokemon_id": "65900"
}

'''response = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_new_pokemons)

print(response.text)'''

'''response_change = requests.patch(url= f'{URL}/pokemons', headers = HEADER, json = body_change)

print(response_change.text)'''

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)

print(response_pokeball.text)

