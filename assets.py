from bs4 import BeautifulSoup
import urllib.request
import pickle
import pathlib


class Assets:
    URL = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
    GENERATIONS = [151, 100, 135, 107, 156, 72, 88, 96, 15]
    FILE_NAME = 'pokedex.pkl'

    def __init__(self, pokemon_count):
        self.count = pokemon_count
        self.data = self.load_pokedex()

    def get_data(self):
        return self.data

    # load from file
    def load_pokedex(self):
        if pathlib.Path(self.FILE_NAME).is_file():
            with open(self.FILE_NAME, 'rb') as file:
                return pickle.load(file)
        # if file dosnt exist create new
        return self._get_data()

    # scrap pokemon name from website
    def _get_data(self):
        web = urllib.request.urlopen(self.URL)
        soup = BeautifulSoup(web.read(), "html.parser")
        table = soup.find(class_='dextable')
        element = table.find_all('tr')
        pokedex = []
        for td in element:
            pokemon = []
            if '#' not in td.text:
                continue
            for td_child in td:
                text = td_child.text.strip()
                if len(text) == 0:
                    continue
                pokemon.append(text)
            id_ = pokemon[0][1:]
            name = pokemon[1]
            stats = pokemon[-6:]
            pokedex.append([id_, name, stats])
        pokedex = self._prepare_data(pokedex)
        with open(self.FILE_NAME, 'wb') as file:
            pickle.dump(pokedex, file)
        return pokedex

    # get only index and name
    def _prepare_data(self, data):
        new_data = []
        pokemon_count = sum(self.GENERATIONS)
        for pokemon in range(pokemon_count):
            new_data.append((data[pokemon][0], data[pokemon][1]))
        return new_data
