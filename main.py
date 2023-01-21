import pygame
from time import sleep, time
from pygame.locals import *
from random import randrange
from pygame import mixer

WIDTH = 1280
HEIGHT = 720
GREEN = (147, 216, 175)

TILE_WIDTH = 100
TILE_HEIGHT = 50

#code to import music
#mixer.init()
#mixer.music.load("_____.mp3") #need to import music into file
#mixer.music.play(-1) #infinitely loops music
#mixer.music.set_volume(0.5) #sets volume to 50%

#might need to figure out a way to stop music when game is closed

def drawTile(screen, x, y, color):
    pygame.draw.polygon(screen, color, ((x, y), (x+49, y+24), (x, y+48), (x-49, y+24)))

def drawImageTile(screen, tile_x, tile_y, image):
    screen.blit(image, (tile_x * TILE_WIDTH + (TILE_WIDTH / 2 if (tile_y % 2) == 0 else 0) - image.get_width() / 2, tile_y * TILE_HEIGHT / 2 - TILE_HEIGHT + 12))

def main():
    pygame.init()
    pygame.display.set_caption("Farming Simulator")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(GREEN)

    running = True

    # fill the screen with tiles
    for i in range(5, 10):
        for j in range(5, 20):
            #drawTile(screen, i * TILE_WIDTH + (TILE_WIDTH / 2 if (j % 2) == 0 else 0), j * TILE_HEIGHT / 2 - TILE_HEIGHT, (randrange(110, 120), randrange(210, 220), randrange(140, 150)))
            drawImageTile(screen, i, j, pygame.image.load("corn_tile.png"))

    # draw the corn tile
    #drawImageTile(screen, 5, 5, pygame.image.load("corn_tile.png"))

    display_surface = pygame.display.get_surface()
    #display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
    pygame.display.flip()


    while running:
        sleep(0.1)


if __name__ == "__main__":
    main()
    