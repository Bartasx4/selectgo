from assets import Assets


class Command:
    REGION = {'kanto': 0, 'johto': 0, 'hoenn': 0, 'sinnoh': 0,
              'unova': 0, 'kalos': 0, 'galar': 0, 'alola': 0}
    RARITY = {'4*': 0, '3*': 0, '2*': 0, '1*': 0, '0*': 0}
    ROCKET = {'rocket': 0, 'shadow': 0, 'purified': 0}
    BOSS = {'legendary': 0, 'mythical': 0, 'hyper beasts': 0}
    NOT_WILD = {'traded': 0, 'raid': 0, 'gbl': 0, 'hatched': 0, 'lucky': 0, 'onlyeggs': 0}
    SPECJAL = {'shiny': 0, 'costume': 0}
    LOW = {'0attack': 0, '0defense': 0, '0stamina': 0}
    SLIDERS = {'from_distance': 0, 'to_distance': 0, 'from_day': 0, 'to_day': 0}
    DESCRIPTION = {'traded': 'z wymiany', 'gbl': 'liga', 'hatched': 'wyklute',
                   'onlyeggs': 'tylko z jajek', 'costume': 'eventowe'}
    GENERATIONS = [151, 100, 135, 107, 156, 72, 88, 96, 15]

    def __init__(self):
        self.pokemon_count = sum(self.GENERATIONS)
        self.toggle_data_pokemons = {self.correct_index(str(index+1)): 0 for index in range(self.pokemon_count)}
        self.toggle_data_other = self.REGION | self.RARITY | self.ROCKET | \
                                 self.BOSS | self.NOT_WILD | self.SPECJAL | self.LOW | self.SLIDERS
        self.toggle_data = self.toggle_data_pokemons | self.toggle_data_other

    @property
    def data(self):
        return self.toggle_data

    @property
    def command(self):
        command = ''
        for raw_key, status in self.toggle_data.items():
            key = raw_key
            if '#' in key:
                key = int(key[1:])
            if status == 0:
                continue
            if len(command) > 0:
                command += '&'
            if status == 1:
                command += key
            elif status == 2:
                command += '!' + key
            else:
                ValueError(self)
        return command

    def pokemon_list(self, generation=0):
        assets = Assets(self.pokemon_count)
        start = sum(self.GENERATIONS[:generation])
        end = sum(self.GENERATIONS[:generation+1])
        pokemon_list = assets.data[start:end]
        status_list = []
        for pokemon in pokemon_list:
            status = self.toggle_data_status(self.correct_index(pokemon[0]))
            status_list.append((pokemon[0], pokemon[1], status))
        return status_list

    def toggle_data_desc(self, data):
        new_data = {}
        for key, status in data.items():
            desc = self.DESCRIPTION[key] if key in self.DESCRIPTION else key
            desc = desc.title()
            new_data[key] = (status, desc)
        return new_data

    def toggle_data_status(self, data):
        option = ''
        if isinstance(data, list):
            option = data[0]
        elif isinstance(data, dict):
            option = list(data.keys())[0]
        elif isinstance(data, str):
            option = data
        match self.toggle_data[option]:
            case 1:
                status = ' show'
            case 2:
                status = ' hide'
            case _:
                status = ''
        return status

    def correct_index(self, number):
        match len(number):
            case 1:
                return '#00' + number
            case 2:
                return '#0' + number
            case 3:
                return '#' + number
            case _:
                return ValueError(self)

    def toggle(self, id_):
        # 0 - none, 1 - select, 2 - ignore
        toggle = self.toggle_data
        toggle[id_] += 1
        if toggle[id_] == 3:
            toggle[id_] = 0
        return toggle[id_]

    def change_slider(self, slider, value):
        self.toggle_data[slider] = value
        return self.data[slider]

    def top_panel(self):
        temp_options = self.RARITY | self.SPECJAL | self.BOSS | self.ROCKET | self.NOT_WILD | self.REGION | self.LOW
        desc_options = self.toggle_data_desc(temp_options)
        # id, status, description, class_status
        options = [(key, value[1], self.toggle_data_status(key)) for key, value in desc_options.items()]
        sliders = {name: self.data[name] for name in self.SLIDERS.keys()}
        return {'options': options, 'sliders': sliders}

    @property
    def save_cookie(self):
        cookie = {}
        for key, status in self.toggle_data.items():
            if status == 0:
                continue
            else:
                cookie[key] = status
        return cookie

    def load_cookie(self, cookie):
        for key, status in cookie.items():
            self.toggle_data[key] = status
