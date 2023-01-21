import pygame
from time import sleep, time
from pygame.locals import *
from random import randrange
from pygame import mixer
import numpy as np
from Map import *
from Constants import *
from Tile import *

def main():
    pygame.init()
    pygame.display.set_caption("Farming Simulator")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    background = pygame.image.load("images/background.png")
    screen.blit(background, (0, 0))
    
    map = Map(0, 0)
    map.render(screen)

    pygame.display.flip()

    while running:
        sleep(1)


if __name__ == "__main__":
    main()
    