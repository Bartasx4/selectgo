from bs4 import BeautifulSoup
import urllib.request
import pickle
from os.path import exists


class Assets:
    URL = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
    GENERATIONS = [151, 100, 135, 107, 156, 72, 88, 96]
    FILE_NAME = 'pokedex.pkl'

    def __init__(self):
        self.data = self.load_pokedex()

    def get_data(self):
        return self.data

    def load_pokedex(self):
        if exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'rb') as file:
                return pickle.load(file)
        return self._get_data()

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

    def _prepare_data(self, data):
        new_data = []
        for index in range(len(self.GENERATIONS)):
            gen = []
            if index == 0:
                r = range(0, 151)
            elif index == len(self.GENERATIONS)-1:
                break
            else:
                r = range(sum(self.GENERATIONS[:index]), sum(self.GENERATIONS[:index+1]))
            for pokemon in r:
                gen.append((data[pokemon][0], data[pokemon][1]))
            new_data.append(gen)
        return new_data
