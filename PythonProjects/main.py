import requests


token = '35c8a2d330a8e9c51c00699a379179e4'

response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                         json = {"name" : "Верон", "photo" : "https://dolnikov.ru/pokemons/albums/010.png"})

print(response.text)

change_pokemon = requests.put('https://pokemonbattle.me:9104/pokemons', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                         json = {"pokemon_id": 6252, "name": "Baunti", "photo": "https://dolnikov.ru/pokemons/albums/010.png"})

print(change_pokemon.text)

pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                         json = {"pokemon_id": 6252})

print(pokeball.text)

kill = requests.post('https://pokemonbattle.me:9104/pokemons/kill', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                         json = {"pokemon_id": 6251})

print(kill.text)


 
