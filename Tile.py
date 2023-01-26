import Constants as c

def getTileLocation(tile):
    tile_x, tile_y = tile
    x =c.WIDTH / 2 + (tile_x * c.TILE_WIDTH / 2 - tile_y * c.TILE_WIDTH / 2)
    y = (tile_y * c.TILE_HEIGHT / 2 + tile_x * c.TILE_HEIGHT / 2)
    return (x, y)

def getCenterTileLocation(tile):
    x, y = getTileLocation(tile)
    y = y + c.TILE_HEIGHT / 4
    return (x, y)

def drawTile(screen, tile, color):
    x, y = getTileLocation(tile)
    c.pygame.draw.polygon(screen, color, ((x, y), (x+c.TILE_HEIGHT-1, y+c.TILE_HEIGHT/2-1), (x, y+c.TILE_HEIGHT-2), (x-c.TILE_HEIGHT-1, y+c.TILE_HEIGHT/2-1)))

def drawTileAlpha(screen, tile, color):
    x, y = getTileLocation(tile)
    points = ((x, y-c.TILE_HEIGHT/2), (x-c.TILE_WIDTH/2,y), (x-c.TILE_WIDTH/2,y+c.TILE_HEIGHT/2), (x, y+c.TILE_HEIGHT), (x+c.TILE_WIDTH/2,y+c.TILE_HEIGHT/2), (x+c.TILE_WIDTH/2,y))
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = c.pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = c.pygame.Surface(target_rect.size, c.pygame.SRCALPHA)
    c.pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    screen.blit(shape_surf, target_rect)

def drawImageTile(screen, tile, image):
    image = c.pygame.transform.scale(image, (c.TILE_WIDTH, c.TILE_WIDTH))
    x, y = getTileLocation(tile)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

def drawBigImageTile(screen, tile, image):
    image = c.pygame.transform.scale(image, (c.TILE_WIDTH*2, c.TILE_WIDTH*2))
    x, y = getTileLocation(tile)
    x  = x - image.get_width() / 2
    y = y - image.get_height() / 2
    screen.blit(image, (x, y))

def getClosestTile(pos):
    # get the closest tile to the mouse
    x, y = pos
    tile_x = int((x -c.WIDTH / 2) / c.TILE_WIDTH + y / c.TILE_HEIGHT)
    tile_y = int(y / c.TILE_HEIGHT - (x -c.WIDTH / 2) / c.TILE_WIDTH)
    return (tile_x, tile_y)