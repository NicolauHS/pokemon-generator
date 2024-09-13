import math

final_stats = {
    "hp":0, 
    "attack":0, 
    "defense":0, 
    "special_attack":0, 
    "special_defense":0, 
    "speed":0
    }

base_stat = {
    "hp":108, 
    "attack":130, 
    "defense":95, 
    "special_attack":80, 
    "special_defense":85, 
    "speed":102
    }

iv = {
    "hp":24, 
    "attack":12, 
    "defense":30, 
    "special_attack":16, 
    "special_defense":23, 
    "speed":5
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

nature = {
    "attack":1.1, 
    "defense":1, 
    "special_attack":0.9, 
    "special_defense":1, 
    "speed":1
    }

name = "Garchomp"

def calculateFinalStats():
    print(name,'\'s final stats are as follows:')
    for stat in final_stats:
        # print(stat, "->", final_stats[stat])

        alpha = (2 * base_stat[stat] + iv[stat] + math.floor(ev[stat]/4))
        # print('2 x', base_stat[stat], '+', iv[stat], '+', ev[stat], '/4')
        beta = math.floor((alpha * level) / 100)

        if stat in "hp":
            calc = math.floor(beta + level + 10)
        else:
            calc = math.floor((beta + 5) * nature[stat])

        # print(calc)
        final_stats[stat] = calc
        
        print(stat, '->', final_stats[stat])

calculateFinalStats()

# calc = math.floor(( ( ((2 * base_stat) + iv + (ev/4) * level) / 100) ) + level + 10)

