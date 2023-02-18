class Farm:
    def __init__(self, name, animals={}):
        self.name = name
        self.animals = animals
    def add_animal(self, animal, qty = 1):
        if animal in self.animals:
            self.animals[animal] += qty
        else:
            self.animals[animal] = qty
    def get_info(self):
        out = f'\n{self.name}\'s farm\n\n'
        for key, val in self.animals.items():
           out += f'{key} : {val}\n'
        out += f'\n     E-I-E-I-0!\n'
        return out
    def get_animal_types(self):
        list_types = [key for key in self.animals]
        list_types.sort()
        return list_types
    def get_short_info(self, list):
        outlist = []
        for item in list:
            outlist.append(item + 's, ')
        outlist[-2] = outlist[-2].replace('s, ', 's and ')
        outlist[-1] = outlist[-1].replace(', ', '.')
        print(outlist)
        out = ''.join(outlist)
        return f"\n{self.name}’s farm has {out}"
mc_donald = Farm("McDonald")
mc_donald.add_animal('cow',5)
mc_donald.add_animal('sheep')
mc_donald.add_animal('sheep')
mc_donald.add_animal('goat', 12)
print(mc_donald.get_info())
print(mc_donald.get_animal_types())
print(mc_donald.get_short_info(mc_donald.get_animal_types()))