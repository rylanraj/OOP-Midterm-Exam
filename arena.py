import csv

from pokemon import Pokemon


class Arena:
    def __init__(self):
        self.pokemons = []

    def add(self, pokemon):
        if not isinstance(pokemon, Pokemon):
            raise AttributeError

        self.pokemons.append(pokemon)

    def active(self):
        active_pokemons = []
        for pokemon in self.pokemons:
            if pokemon.health > 0:
                active_pokemons.append(pokemon)

        return active_pokemons

    def get_pokemons(self):
        return self.pokemons

    def load_from_file(self, filename):
        with open(filename) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if csv_reader.line_num is not 1:
                    pokemon = Pokemon(name=row[0], health=int(row[1]))
                    pokemon.set_level(int(row[2]))
                    self.add(pokemon)

    def __len__(self):
        return len(self.active())



