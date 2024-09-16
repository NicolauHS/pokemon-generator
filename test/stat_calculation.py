# Tests if stats are calculated correctly using example from bulbapedia
from math import floor

final_dictionary = {}

def calculate_stat(stat, base_value, iv, ev, level, nature_good_stat, nature_bad_stat):    

    try:
        alpha = (2 * base_value + iv + floor(ev/4))
        beta = floor((alpha * level)/100)

        if "hp" in stat:
            delta = beta + level + 10
            # final_hp = delta
            final_dictionary[stat] = delta
        else: 
            delta = beta + 5
            if stat == nature_good_stat:
                final_dictionary[stat] = floor(delta * 1.1)
            elif stat == nature_bad_stat:
                # final_value = floor(delta * 0.9)
                final_dictionary[stat] = floor(delta * 0.9)
            else:
                # final_value = floor(delta)
                final_dictionary[stat] = floor(delta)
        
    except Exception as e:
        print("Error while calculating stats")
        print("Error:", e)

level = 78

calculate_stat("hp", 108, 24, 74, level, "attack", "special_attack")
calculate_stat("attack", 130, 12, 190, level, "attack", "special_attack")
calculate_stat("defense", 95, 30, 91, level, "attack", "special_attack")
calculate_stat("special_attack", 80, 16, 48, level, "attack", "special_attack")
calculate_stat("special_defense", 85, 23, 84, level, "attack", "special_attack")
calculate_stat("speed", 102, 5, 23, level, "attack", "special_attack")

# print(final_dictionary)
for stat in final_dictionary:
    print(stat, '->', final_dictionary[stat])

# TESTED AND IT WORKS