

class Command:
	
	def __init__(self, pokemon_count):
		self.toggle_data = [f'#{index}' for index in range(pokemon_count)]
		self.toggle_data |= {'kanto': 0, 'johto': 0, 'hoenn': 0, 'sinnoh': 0, 'unova': 0, 'kalos': 0, 'galar': 0, 'alola': 0}
		self.toggle_data |= {'4*': 0, '3*': 0, '2*': 0, '1*': 0, '0*': 0,
                             'shiny': 0, 'legendary': 0, 'mythical': 0, 'hyper beasts': 0, 'shadow': 0,
                             'purified': 0, 'lucky': 0, 'traded': 0, 'hatched': 0, 'raid': 0, 'gbl': 0,
                             'costume': 0, 'alolan': 0, 'galar': 0, 'onlyeggs': 0, 'defender': 0,
                             'xlcandy': 0, 'evolvenew': 0, '0attack': 0, '0defense': 0, '0stamina': 0}
		
	@property
	def command(self):
		command = ''
		for key, status in self.toggle_data.items():
			if status == 0:
				continue
			if len(command) > 0:
				command += '&'
			if status == 2:
				command += '!'
			if '#' in key:
				command += key[1:]
			else:
				command += key
		return command
	
	@property	
	def data(self):
		return self.toggle_data
		
	def toggle(self, id_):
	   # 0 - none, 1 - select, 2 - ignore
	   toggle = self.toggle_data
	   toggle[id_] += 1
	   if toggle[id_] == 3:
	       toggle[id_] = 0
	   return toggle[id_]