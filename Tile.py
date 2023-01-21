from Constants import *
import pygame

def getTileLocation(tile_x, tile_y):
    x = WIDTH / 2 + (tile_x * TILE_WIDTH / 2 - tile_y * TILE_WIDTH / 2)
    y = (tile_y * TILE_HEIGHT / 2 + tile_x * TILE_HEIGHT / 2)
    return (x, y)

def drawTile(screen, tile_x, tile_y, color):
    x, y = getTileLocation(tile_x, tile_y)
    pygame.draw.polygon(screen, color, ((x, y), (x+TILE_HEIGHT-1, y+TILE_HEIGHT/2-1), (x, y+TILE_HEIGHT-2), (x-TILE_HEIGHT-1, y+TILE_HEIGHT/2-1)))

def drawImageTile(screen, tile_x, tile_y, image):
    image = pygame.transform.scale(image, (TILE_WIDTH, TILE_WIDTH))
    x, y = getTileLocation(tile_x, tile_y)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

def drawBigImageTile(screen, tile_x, tile_y, image):
    image = pygame.transform.scale(image, (TILE_WIDTH*2, TILE_WIDTH*2))
    x, y = getTileLocation(tile_x, tile_y)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

class Tile():
    def __init__(self, type, price, count, x, y):
        self.type = type
        self.count = count
        self.price = price
        self.x = x
        self.y = y
        self.weather = self.calculateWeather()
        self.terrain = self.calculateTerrain()

    def updatePrice(self):
        pass
    
class Corn(Tile):
    def __init__(self, x, y):
        super().__init__("corn", 5, 10, x, y)

class Weed(Tile):
    def __init__(self, x, y):
        super().__init__("weed", -10, 1, x, y)

class Rock(Tile):
    def __init__(self, x, y):
        super().__init__("rock", -1000, 1, x, y)