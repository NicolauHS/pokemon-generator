#!/usr/bin/env python3
from Pokemon import Pokemon
import json
import random as r
import pygame

def pretty_print(obj):
    obj = vars(obj)

    print(json.dumps(obj, indent=4))

    return

def main():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

    pygame.quit()

    # randomize a pokemon
    numbers = [0, 1, 2, 3, 4]
    id_chosen = r.choice(numbers)
    print(id_chosen)
    poke_1 = Pokemon(species_id=None, level=5)

    pretty_print(poke_1)

    # poke_1.rename("Toninho")

    # pretty_print(poke_1)

if __name__ == "__main__":
    main()
