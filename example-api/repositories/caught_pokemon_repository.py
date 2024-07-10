import requests
from models.pokemon import Pokemon

class CaughtPokemonRepository:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5001/pokemon"

    def get_caught_pokemon(self) -> list[Pokemon]:
        # This method should return a list of caught Pokemon from the database.
        response = requests.get(self.base_url)
        caught_pokemon = []
        if response.status_code == 200:
            pokemon_data = response.json()
            for pokemon in pokemon_data:
                name = pokemon["name"]
                type = pokemon["type"]
                abilities = pokemon["abilities"]
                height = pokemon["height"]
                weight = pokemon["weight"]
                image = pokemon["image"]
                caught_pokemon.append(Pokemon(name, type, abilities, height, weight, image))
        return caught_pokemon

    def catch_pokemon(self, pokemon: Pokemon):
        # This method should add a caught Pokemon to the database.
        data = {
            "name": pokemon.name,
            "type": pokemon.type,
            "abilities": pokemon.abilities,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image": pokemon.image
        }
        response = requests.post(self.base_url, json=data)
        return response.status_code == 200
