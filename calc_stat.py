import math
import random
import json

###### IV GENERATION #################################################

def generate_ivs():
 
    iv_dictionary = {
        "hp":0,
        "attack":0,
        "defense":0,
        "special_attack":0,
        "special_defense":0,
        "speed":0
    }
    for stat in iv_dictionary:
        iv_dictionary[stat] = random.randint(0,31)
        # print(stat, '->', iv_dictionary[stat])
    
    return iv_dictionary

######################################################################

###### NATURE ########################################################

def choose_random_json_elem(file):
    with open(file, 'r') as file:
        data = json.load(file)
        random_key = random.choice(list(data.keys()))
        random_element = data[random_key]
        return random_element
    
######################################################################
# print(nature)

# nature_name = nature['name']
# nature_positive_stat = None
# nature_negative_stat = None
# favorite_flavor = None
# disliked_flavor = None

# if nature['increased_stat']:
#     nature_positive_stat = nature['increased_stat']

# if nature['decreased_stat']:
#     nature_positive_stat = nature['decreased_stat']

# if nature['increased_stat']:
#     nature_positive_stat = nature['increased_stat']

# if nature['increased_stat']:
#     nature_positive_stat = nature['increased_stat']

######################################################################

def calculate_final_stats(base_stat, iv, ev, nature, level):

    final_stats = {
    "hp":0, 
    "attack":0, 
    "defense":0, 
    "special_attack":0, 
    "special_defense":0, 
    "speed":0
    }

    name = "Garchomp"

    print(name,'\'s final stats are as follows:')

    if "increased_stat" in nature:
        inc_stat = nature["increased_stat"]

    if "decreased_stat" in nature:
        dec_stat = nature["decreased_stat"]

    for stat in final_stats:
        try:
            alpha = (2 * base_stat[stat] 
                    + iv[stat] 
                    + math.floor(ev[stat]/4))
            beta = math.floor((alpha * level) / 100)

            if stat in "hp":
                calc = math.floor(beta + level + 10)
            
            elif ("increased_stat" in nature and 
                  stat == inc_stat):    
                calc = math.floor((beta + 5) * 1.1)
            
            elif ("decreased_stat" in nature and 
                  stat == dec_stat):    
                calc = math.floor((beta + 5) * 0.9)
            
            else:                
                calc = math.floor((beta + 5))
            
            final_stats[stat] = calc
            
            print(stat, '->', final_stats[stat])
        except KeyError as e:
            print(f"KeyError: {e}")
        except TypeError as e:
            print(f"TypeError: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return final_stats

def main():
    # Placeholder base stats for a Garchomp
    # Also placeholder ev and level

    base_stat = {
        "hp":108, 
        "attack":130, 
        "defense":95, 
        "special_attack":80, 
        "special_defense":85, 
        "speed":102
        }
        
    ev = {
        "hp":74, 
        "attack":190,
        "defense":91, 
        "special_attack":48, 
        "special_defense":84, 
        "speed":23
        }

    level = 78

    iv = generate_ivs()
    nature = choose_random_json_elem('pkmn_nature.json')
    final_stats = calculate_final_stats(base_stat, iv, ev, nature, level)

    print('Nature:', nature['name'])
    print(final_stats)        

if __name__:
    main()