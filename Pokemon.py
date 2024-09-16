import json
import random
from random import randint
# import math
from math import floor
# import numpy as np


class Pokemon:

    def set_iv_rating(self, iv):
        if iv <= 2:
            return "Terrible"
        elif iv >= 3 and iv <= 7:
            return "Bad"
        elif iv >= 8 and iv <= 13:
            return "Poor"
        elif iv >= 14 and iv <= 18:
            return "Average"
        elif iv >= 19 and iv <= 24:
            return "Good"
        elif iv >=25 and iv <= 28:
            return "Excellent"
        elif iv >= 29:
            return "Perfect"
        
    def calculate_stats(self):
        # Simulates the stat calculation of gen 3 onwards, 
        # separates the equation in small parts

        # Dictionaries are used to make all the stat calculations in one go 
        # and not having to call it once for each stat
        try:
            stat_array = ["hp", 
                        "attack", 
                        "defense", 
                        "special_attack", 
                        "special_defense", 
                        "speed"]
            
            base_dictionary = {
                "hp": self.base_hp,
                "attack": self.base_attack,
                "defense": self.base_defense,
                "special_attack": self.base_special_attack,
                "special_defense": self.base_special_defense,
                "speed": self.base_speed
            }

            iv_dictionary = {
                "hp": self.hp_iv,
                "attack": self.attack_iv,
                "defense": self.defense_iv,
                "special_attack": self.special_attack_iv,
                "special_defense": self.special_defense_iv,
                "speed": self.speed_iv
            }

            ev_dictionary = {
                "hp": self.hp_ev,
                "attack": self.attack_ev,
                "defense": self.defense_ev,
                "special_attack": self.special_attack_ev,
                "special_defense": self.special_defense_ev,
                "speed": self.speed_ev
            }

            # final_dictionary = {
            #     "hp": "final_hp",
            #     "attack": "final_attack",
            #     "defense": "final_defense",
            #     "special_attack": "final_special_attack",
            #     "special_defense": "final_special_defense",
            #     "speed": "final_speed"
            # }

            final_dictionary = {
               
            }

        except Exception as e:
            print(f"Error when declaring dictionary variables in stat calculation")
            print(f"Error:", e)
            return False
        
        try:
            for stat in stat_array:
                base_value = base_dictionary[stat]
                iv = iv_dictionary[stat]
                ev = ev_dictionary[stat]

                alpha = (2 * base_value + iv + floor(ev/4))
                beta = floor((alpha * self.level)/100)

                if "hp" in stat:
                    delta = beta + self.level + 10
                    # self.final_hp = delta
                    final_dictionary[stat] = delta
                else: 
                    delta = beta + 5
                    if stat == self.nature_good_stat:
                        final_dictionary[stat] = floor(delta * 1.1)
                    elif stat == self.nature_bad_stat:
                        # self.final_value = floor(delta * 0.9)
                        final_dictionary[stat] = floor(delta * 0.9)
                    else:
                        # self.final_value = floor(delta)
                        final_dictionary[stat] = floor(delta)
        except Exception as e:
            print("Error while calculating stats")
            print("Error:", e)

        # OK, after all that, it now applies the values to the pokemons stats
        self.hp = final_dictionary["hp"]
        self.attack = final_dictionary["attack"]
        self.defense = final_dictionary["defense"]
        self.special_attack = final_dictionary["special_attack"]
        self.special_defense = final_dictionary["special_defense"]
        self.speed = final_dictionary["speed"]

    def __init__(self, species_id, level, name=None): 

        self.level = level
        self.species_id = species_id
        self.name = name
        self.type = None
        self.fainted = False
        self.active_in_battle = False

        # STATS

        try:
            with open('ref/pkmn_species.json', 'r') as species_info:
                species_data = json.load(species_info)[str(species_id)]
                
                if name == None:
                    self.name = species_data["species_name"]

                self.type = species_data["type"]
                if "sec_type" in species_data:
                    self.secondary_type = species_data["sec_type"]

                self.base_hp = species_data["hp"]
                self.base_attack = species_data["attack"]
                self.base_defense = species_data["defense"]
                self.base_special_attack = species_data["special_attack"]
                self.base_special_defense = species_data["special_defense"]
                self.base_speed = species_data["speed"]

        except Exception as e:
            print(f"Error fetching Pokémon species information: {e}")
            print(f"Pokemon species: ", species_id)
        
        # NATURE

        try:
            with open('ref/pkmn_nature.json', 'r') as nature_list:
                random_index = randint(0, 24)
                # random_index = 0
                nature_data = json.load(nature_list)[str(random_index)]

                self.nature_name = nature_data["nature"]
                self.nature_good_stat = "None"
                self.nature_bad_stat = "None"
                self.favorite_flavor = "None"
                self.disliked_flavor = "None"

                if "increased_stat" in nature_data:
                    self.nature_good_stat = nature_data["increased_stat"]
                
                if "decreased_stat" in nature_data:
                    self.nature_bad_stat = nature_data["decreased_stat"]

                if "favorite_flavor" in nature_data:                    
                    self.favorite_flavor = nature_data["favorite_flavor"]

                if "disliked_flavor" in nature_data:
                    self.disliked_flavor = nature_data["disliked_flavor"]
        
        except Exception as e:
            print(f"Error fetching Pokémon nature: {e}")

        # IVs

        self.hp_iv = random.randint(0, 15) + random.randint(0,16)
        self.attack_iv = random.randint(0, 15) + random.randint(0,16)
        self.defense_iv = random.randint(0, 15) + random.randint(0,16)
        self.speed_iv = random.randint(0, 15) + random.randint(0,16)
        self.special_attack_iv = random.randint(0, 15) + random.randint(0,16)
        self.special_defense_iv = random.randint(0, 15) + random.randint(0,16)

        # EVs

        self.hp_ev = 0
        self.attack_ev = 0
        self.defense_ev = 0
        self.speed_ev = 0
        self.special_attack_ev = 0
        self.special_defense_ev = 0

        # FINAL STATS

        self.calculate_stats()

    def rename(self, new_name):
        self.name = new_name

    # def attack():
    #     # pkmn does the normal attack
    #     pass

    def use_move(move_name):
        # searches for move in pkmn_moves.json, attacks using that move
        # calculates damage applying modifiers of attacker type and attack type
        # and receiver type to attack type.
        # modifiers can be found in pkmn_type_interaction.json
        pass

    def faint():
        # pkmn faints
        fainted = True
        pass

    def level_up():
        # pkmn levels up and its stats increase based on EV and poke_lvlup.json
        # checks if out of combat, then proceeds

        # checks if pokemon is in equal or above evolving level, if so, 
        # calls evolve()
        pass

    def evolve():
        # consult pkmn_lvlup.json for their species_id and turn it into the
        # value in parameter "evolves_to" and apply stat calculations for the
        # new evolution
        pass

