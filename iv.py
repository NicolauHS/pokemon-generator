#!/usr/bin/env python3

import random
# import math
import numpy as np
from decimal import Decimal as D
from decimal import getcontext


getcontext().prec = 2
# iv_spread = []
# iv_results = []

def generate_iv_spread():
    iv_spread = []
    # Repeat 5 times for each stat
    for i in range(5):
        # Generate random number between 0 and 0.50 modified by the equalizer
        iv_generated = round(random.random()*50)/100

        # Append it to the list of IV's
        iv_spread.append(round(0.75 + iv_generated, 2))

    iv_spread_mean = np.mean(iv_spread)

    if iv_spread_mean < .95:
        hidden_trait = "Determined"
    elif iv_spread_mean > 1.05:
        hidden_trait = "Apathetic"
    else:
        hidden_trait = None

    return iv_spread, iv_spread_mean, hidden_trait    

def set_iv_rating(iv):
    if iv < .85:
        return "Bad"
    elif iv >= .85 and iv < .95:
        return "Below average"
    elif iv >= .95 and iv <= 1.05:
        return "Average"
    elif iv > 1.05 and iv <= 1.15:
        return "Above average"
    elif iv > 1.15:
        return "Excellent"

def assign_iv_to_stats():
    global hidden_trait  # Add global declaration for hidden_trait
    hp_iv = iv_spread[0]
    attack_iv = iv_spread[1]
    defense_iv = iv_spread[2]
    speed_iv = iv_spread[3]
    special_iv = iv_spread[4]
    return hp_iv, attack_iv, defense_iv, speed_iv, special_iv

def show_stats():
    print('-----STATS-----')
    hp_iv, attack_iv, defense_iv, speed_iv, special_iv = assign_iv_to_stats()
    hp_rating = set_iv_rating(hp_iv)
    attack_rating = set_iv_rating(attack_iv)
    defense_rating = set_iv_rating(defense_iv)
    speed_rating = set_iv_rating(speed_iv)
    special_rating = set_iv_rating(special_iv)

    print('HP:', hp_rating)
    print('ATT:', attack_rating)
    print('DEF:', defense_rating)
    print('SPD:', speed_rating)
    print('SPE:', special_rating)

    print('\n')
    print('*detailed stats*')
    print('-----IVs------')
    print("HP:", hp_iv)
    print("ATT:", attack_iv)
    print("DEF:", defense_iv)
    print("SPD:", speed_iv)
    print("SPE:", special_iv)
    print('\n')
    print("AVG:", round(iv_spread_mean, 2))

    if hidden_trait:
        print("Trait:", hidden_trait)
    else:
        print("Trait: None")

iv_spread, iv_spread_mean, hidden_trait = generate_iv_spread()
show_stats()