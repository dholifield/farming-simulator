from random import randrange
import pygame
import numpy as np
from Constants import *
from Tile import *

class Map():
    def __init__(self, lat, lon):
        self.tiles = np.zeros((25, 25))
        self.lat = lat
        self.lon = lon
        self.generateTerrain()

    def calculateWeather(self):
        pass

    def calculateTerrain(self):
        pass

    def generateTerrain(self):
        # fill everything with dirt
        for i in range(1, 24):
            for j in range(1, 24):
                self.tiles[i][j] = 1

        # randomly add 10 rocks to the map
        for i in range(0, 10):
            self.tiles[randrange(1, 24)][randrange(1, 24)] = 2

    def draw(self, screen):
        for i in range(0, 25):
            for j in range(0, 25):
                drawTile(screen, i, j, (randrange(110, 120), randrange(210, 220), randrange(140, 150)))
                if self.tiles[i][j] == 0:
                    drawImageTile(screen, i, j, pygame.image.load("images/grass.png"))
                elif self.tiles[i][j] == 1:
                    drawImageTile(screen, i, j, pygame.image.load("images/dirt.png"))
                elif self.tiles[i][j] == 2:
                    # random boolean to determine if rock is on the left or right
                    rock = pygame.image.load("images/rock.png")
                    if randrange(0, 2) == 0:
                        rock = pygame.transform.flip(rock, True, False)
                    drawImageTile(screen, i, j, rock)

    def drawBackground(selfm, screen):
        screen.blit(pygame.image.load("images/background.png"), (0, 0))
    
    def generateBackrgound(self, screen):
           # generate background image
            for i in range(0, 13):
                for j in range(-7, 0):
                    drawBigImageTile(screen, 2*j, 2*i, pygame.image.load("images/tree.png"))
                    drawBigImageTile(screen, 2*i, 2*j, pygame.image.load("images/tree.png"))

            for i in range(0, 25):
                for j in range(25, 40):
                    drawImageTile(screen, i, j, pygame.image.load("images/grass.png"))
                    drawImageTile(screen, j, i, pygame.image.load("images/water.png"))

            for i in range (0, 25):
                drawImageTile(screen, 25, i, pygame.image.load("images/grass.png"))
                drawImageTile(screen, 26, i, pygame.image.load("images/grass.png"))
                drawImageTile(screen, 27, i, pygame.image.load("images/dirt.png"))

            barn = pygame.image.load("images/barn.png")
            barn = pygame.transform.scale(barn, (400, 350))
            screen.blit(barn, (5, 550))
