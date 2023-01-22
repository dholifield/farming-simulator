from random import randrange
import pygame
import numpy as np
import Constants as c
from Tile import *



class Map():
    def __init__(self, lat, lon):
        self.tiles = np.zeros((25, 25))
        self.sprout_times = np.zeros((25, 25))
        self.lat = lat
        self.lon = lon
        self.generateTerrain()
        self.grass_image = pygame.image.load("images/grass.png").convert_alpha()
        self.dirt_image = pygame.image.load("images/dirt.png").convert_alpha()
        self.rock_image = pygame.image.load("images/rock.png").convert_alpha()
        self.corn_image = pygame.image.load("images/corn.png").convert_alpha()
        self.sprout_image = pygame.image.load("images/sprout.png").convert_alpha()
        self.background = pygame.image.load("images/background.png").convert()

    def calculateWeather(self):
        pass

    def calculateTerrain(self):
        pass

    def generateTerrain(self):
        # fill everything with dirt
        for i in range(1, 24):
            for j in range(1, 24):
                self.tiles[i][j] = 3

        # randomly add 10 rocks to the map
        for i in range(0, 20):
            self.tiles[randrange(1, 24)][randrange(1, 24)] = 2

    def update(self, harvester, planter):
        harvester_tile = getClosestTile((harvester.x, harvester.y))
        planter_tile = getClosestTile((planter.x, planter.y))
        if harvester_tile[0] >= 0 and harvester_tile[0] < 25 and harvester_tile[1] >= 0 and harvester_tile[1] < 25:
            if self.tiles[harvester_tile[0]][harvester_tile[1]] == 3:
                self.tiles[harvester_tile[0]][harvester_tile[1]] = 1
                c.corn_count += c.CORN_TILE_AMOUNT
            if self.tiles[harvester_tile[0]][harvester_tile[1]] == 2:
                c.corn_count /= 2
        if planter_tile[0] >= 0 and planter_tile[0] < 25 and planter_tile[1] >= 0 and planter_tile[1] < 25:
            if self.tiles[planter_tile[0]][planter_tile[1]] == 1:
                if c.balance >= c.SEED_COST:
                    self.tiles[planter_tile[0]][planter_tile[1]] = 4
                    c.balance -= c.SEED_COST

    def draw(self, screen):
        for i in range(0, 25):
            for j in range(0, 25):
                if self.tiles[i][j] == 0:
                    drawImageTile(screen, (i, j), self.grass_image)
                elif self.tiles[i][j] == 1:
                    drawImageTile(screen, (i, j), self.dirt_image)
                elif self.tiles[i][j] == 2:
                    drawImageTile(screen, (i, j), self.rock_image)
                elif self.tiles[i][j] == 3:
                    drawImageTile(screen, (i, j), self.corn_image)
                elif self.tiles[i][j] == 4:
                    drawImageTile(screen, (i, j), self.sprout_image)

    def drawBackground(self, screen):
        screen.blit(self.background, (0, 0))
    
    def generateBackrgound(self, screen):
           # generate background image
            for i in range(0, 13):
                for j in range(-7, 0):
                    drawBigImageTile(screen, (2*j, 2*i), pygame.image.load("images/tree.png"))
                    drawBigImageTile(screen, (2*i, 2*j), pygame.image.load("images/tree.png"))

            for i in range(0, 25):
                for j in range(25, 40):
                    drawImageTile(screen, (i, j), pygame.image.load("images/grass.png"))
                    drawImageTile(screen, (j, i), pygame.image.load("images/water.png"))

            for i in range (0, 25):
                drawImageTile(screen, (25, i), pygame.image.load("images/grass.png"))
                drawImageTile(screen, (26, i), pygame.image.load("images/grass.png"))
                drawImageTile(screen, (27, i), pygame.image.load("images/dirt.png"))

            barn = pygame.image.load("images/barn.png")
            barn = pygame.transform.scale(barn, (400, 350))
            screen.blit(barn, (5, 550))
