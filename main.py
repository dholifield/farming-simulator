import pygame
from time import sleep, time
from pygame.locals import *
from random import randrange
from pygame import mixer
import numpy as np
from Map import *
import Constants as c
from Tile import *
from Tractor import *
from Info import *

def main():
    pygame.init()
    pygame.display.set_caption("Farming Simulator")
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))

    map = Map(0, 0)
    map.drawBackground(screen)
    map.draw(screen)

    harvester = Tractor("harvester", pygame.K_1, (480, 800))
    planter = Tractor("planter", pygame.K_2, (400, 850))
    path = Path()
    info = Info()

    pygame.display.flip()

    while 1:
        t0 = time()

        # stop the game if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        map.drawBackground(screen)
        map.update(harvester, planter)
        map.draw(screen)

        path.update(screen, mouse, click)

        harvester.update(path)
        harvester.draw(screen)

        planter.update(path)
        planter.draw(screen)

        info.update()
        info.draw(screen)
        info.sellCornButton(mouse, click)

        pygame.display.flip()

        tf = time()

        dt = tf - t0
        if dt < 1/60:
            sleep(1/60 - dt)
        #print(1/dt)
    # end while

if __name__ == "__main__":
    main()
    