import pygame
from time import sleep, time
from pygame.locals import *
from random import randrange
from pygame import mixer
import numpy as np
from Map import *
from Constants import *
from Tile import *
from Tractor import *

def main():
    pygame.init()
    pygame.display.set_caption("Farming Simulator")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    
    map = Map(0, 0)
    map.drawBackground(screen)
    map.draw(screen)

    tractor = Tractor()

    pygame.display.flip()

    while running:
        # stop the game if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        map.drawBackground(screen)

        tractor.update()
        

if __name__ == "__main__":
    main()
    