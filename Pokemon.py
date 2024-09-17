import json
import random
# import math
import numpy as np


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

    def __init__(self, species_id, level, name=None): 

        self.level = level
        self.species_id = species_id
        self.name = name
        self.type = None
        self.fainted = False

        # STATS

        self.base_hp = None
        self.base_attack = None
        self.base_defense = None        
        self.base_special_attack = None
        self.base_special_defense = None
        self.base_speed = None
        
        # GENERATE IVs

        self.hp_iv = random.randint(0, 31)
        self.attack_iv = random.randint(0, 31)
        self.defense_iv = random.randint(0, 31)
        self.speed_iv = random.randint(0, 31)
        self.special_attack_iv = random.randint(0, 31)            
        self.special_defense_iv = random.randint(0, 31)            

        try:
            with open('ref/pkmn_species.json') as species_info:
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
            print(f"Error: {e}")

        # self.health_points = generate_iv(health)
        # Generate IVs
        # Grab species and stats from poke_stats
        # Calculate final stats being modified by level and IVs

    def rename(self, new_name):
        self.name = new_name

    def attack():
        # pkmn does the normal attack
        pass

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

