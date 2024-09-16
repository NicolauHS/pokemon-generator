#!/usr/bin/env python3
from Pokemon import Pokemon
import json
import random as r
# import pygame

def pretty_print(obj):
    obj = vars(obj)

    print(json.dumps(obj, indent=4))

    return

def main():

    dict = {
        '0': {},
        '1': {},
        '2': {},
        '3': {},
        '4': {}
    }

    id_chosen = r.choice(range(151))
    level_chosen = r.choice(range(5,10))
    poke_1 = Pokemon(species_id=id_chosen, level=level_chosen)
    dict['0'] = poke_1.__dict__

    id_chosen = r.choice(range(151))
    level_chosen = r.choice(range(5,99))
    poke_2 = Pokemon(species_id=id_chosen, level=level_chosen)
    dict['1'] = poke_2.__dict__

    id_chosen = r.choice(range(151))
    level_chosen = r.choice(range(5,99))
    poke_3 = Pokemon(species_id=id_chosen, level=level_chosen)
    dict['2'] = poke_3.__dict__

    # id_chosen = r.choice(range(151))
    # level_chosen = r.choice(range(5,99))
    # poke_4 = Pokemon(species_id=id_chosen, level=level_chosen)
    # dict['3'] = poke_4.__dict__

    # print(dict['0']['name'])

    for pokemon in dict.values():
        if 'name' in pokemon:
            level = "%02d" % pokemon['level']
            print(f"Lv {level} {pokemon['name']} with {pokemon['nature_name']} nature")
            print("      └--> HP:         ", pokemon['hp'])
            print("      └--> Attack:     ", pokemon['attack'])
            print("      └--> Defense:    ", pokemon['defense'])
            print("      └--> Sp. Attack: ", pokemon['special_attack'])
            print("      └--> Sp. Defense:", pokemon['special_defense'])
            print("      └--> Speed:      ", pokemon['speed'])
        else:
            print('-----------')


        # print(pokemon)
        # print(f"{pokemon['name']} | Lv {pokemon['level']}")
        pass

    # poke_1.rename("Toninho")

    # pretty_print(poke_1)

if __name__ == "__main__":
    main()
