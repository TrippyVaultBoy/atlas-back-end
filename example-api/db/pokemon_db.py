import sqlite3
from models.pokemon import Pokemon

class PokemonDB:
    def __init__(self):
        self.connection = sqlite3.connect("db/pokemon.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        query = "CREATE TABLE IF NOT EXISTS pokemon (name TEXT PRIMARY KEY, type TEXT, abilities TEXT, height INTEGER, weight INTEGER, image TEXT)"
        self.cursor.execute(query)

    def get_caught_pokemon(self) -> list[Pokemon]:
        query = "SELECT * FROM pokemon"
        self.cursor.execute(query)
        pokemon_data = self.cursor.fetchall()
        caught_pokemon = []
        for pokemon in pokemon_data:
            name, type, abilities, height, weight, image = pokemon
            caught_pokemon.append(Pokemon(name, type, abilities, height, weight, image))
        return caught_pokemon

    def catch_pokemon(self, pokemon: Pokemon):
        query = "INSERT INTO pokemon (name, type, abilities, height, weight, image) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (pokemon.name, pokemon.type, pokemon.abilities, pokemon.height, pokemon.weight, pokemon.image))
        self.connection.commit()

    def close(self):
        self.connection.close()

