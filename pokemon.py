import pypokedex
import json

# cards to add
size = 18
name_list = []
dex_list = []

# load pokedex
with open('pokedex.json') as json_file:
    pokedex = json.load(json_file)
# changes keys to int
pokedex2={}
for key in pokedex.keys():
  pokedex2[int(key)] = pokedex[key]
pokedex=pokedex2

# add cards
for NAME in name_list:
  pokemon = pypokedex.get(name=NAME)
  if (pokemon.dex%18 == 0): pokedex[int(pokemon.dex)]=[pokemon.name, pokemon.dex, pokemon.dex//size-1, size]
  else: pokedex[int(pokemon.dex)]=[pokemon.name, pokemon.dex, pokemon.dex//size, pokemon.dex%size]
for DEX in dex_list:
  pokemon = pypokedex.get(dex=DEX)
  if (pokemon.dex%18 == 0): pokedex[int(pokemon.dex)]=[pokemon.name, pokemon.dex, pokemon.dex//size-1, size]
  else: pokedex[int(pokemon.dex)]=[pokemon.name, pokemon.dex, pokemon.dex//size, pokemon.dex%size]


# sort and print
pokedex = dict(sorted(pokedex.items()))
for pokemon in pokedex.items():
  print(pokemon)
print('------------------------------')
print('TOT ' + str(len(pokedex.items())))

# save pokedex
with open("pokedex.json", "w") as fp:
    json.dump(pokedex, fp)
