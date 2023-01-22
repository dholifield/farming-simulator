from Constants import *
import pygame

def getTileLocation(tile):
    tile_x, tile_y = tile
    x = WIDTH / 2 + (tile_x * TILE_WIDTH / 2 - tile_y * TILE_WIDTH / 2)
    y = (tile_y * TILE_HEIGHT / 2 + tile_x * TILE_HEIGHT / 2)
    return (x, y)

def getCenterTileLocation(tile):
    x, y = getTileLocation(tile)
    y = y + TILE_HEIGHT / 4
    return (x, y)

def drawTile(screen, tile, color):
    x, y = getTileLocation(tile)
    pygame.draw.polygon(screen, color, ((x, y), (x+TILE_HEIGHT-1, y+TILE_HEIGHT/2-1), (x, y+TILE_HEIGHT-2), (x-TILE_HEIGHT-1, y+TILE_HEIGHT/2-1)))

def drawTileAlpha(screen, tile, color):
    x, y = getTileLocation(tile)
    points = ((x, y-TILE_HEIGHT/2), (x-TILE_WIDTH/2,y), (x-TILE_WIDTH/2,y+TILE_HEIGHT/2), (x, y+TILE_HEIGHT), (x+TILE_WIDTH/2,y+TILE_HEIGHT/2), (x+TILE_WIDTH/2,y))
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    screen.blit(shape_surf, target_rect)

def drawImageTile(screen, tile, image):
    image = pygame.transform.scale(image, (TILE_WIDTH, TILE_WIDTH))
    x, y = getTileLocation(tile)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

def drawBigImageTile(screen, tile, image):
    image = pygame.transform.scale(image, (TILE_WIDTH*2, TILE_WIDTH*2))
    x, y = getTileLocation(tile)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

def getClosestTile(pos):
    # get the closest tile to the mouse
    x, y = pos
    tile_x = int((x - WIDTH / 2) / TILE_WIDTH + y / TILE_HEIGHT)
    tile_y = int(y / TILE_HEIGHT - (x - WIDTH / 2) / TILE_WIDTH)
    return (tile_x, tile_y)

class Tile():
    def __init__(self, type, image, price, count, x, y):
        self.image = image
        self.type = type
        self.count = count
        self.price = price
        self.x = x
        self.y = y
        self.weather = self.calculateWeather()

    def draw(self, screen):
        drawImageTile(screen, self.x, self.y, self.image)

    def updatePrice(self):
        pass

class Dirt(Tile):
    def __init__(self, x, y):
        super().__init__("dirt", pygame.image.load("images/dirt.png").convert_alpha(), 0, 0, x, y)

class Grass(Tile):
    def __init__(self, x, y):
        super().__init__("grass", pygame.image.load("images/grass.png").convert_alpha(), 0, 0, x, y)
    
class Corn(Tile):
    def __init__(self, x, y):
        super().__init__("corn", pygame.image.load("images/corn.png").convert_alpha(), 5, 10, x, y)

class Rock(Tile):
    def __init__(self, x, y):
        super().__init__("rock", pygame.image.load("images/rock.png").convert_alpha(), -1000, 1, x, y)

# class Weed(Tile):
#      def __init__(self, x, y):
#         super().__init__("weed", pygame.image.load("images/weed.png").convert_alpha(), -10, 1, x, y)