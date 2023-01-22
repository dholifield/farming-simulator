import pygame
import math
import numpy as np
import Constants as c
from Tile import *

class Tractor():
    def __init__(self, type, button, start):
        self.type = type
        self.button = button
        self.image0 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"0.png").convert_alpha(), (178, 100))
        self.image45 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"45.png").convert_alpha(), (178, 100))
        self.image90 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"90.png").convert_alpha(), (178, 100))
        self.image135 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"135.png").convert_alpha(), (178, 100))
        self.image180 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"180.png").convert_alpha(), (178, 100))
        self.image225 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"225.png").convert_alpha(), (178, 100))
        self.image270 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"270.png").convert_alpha(), (178, 100))
        self.image315 = pygame.transform.scale(pygame.image.load("images/"+self.type+"/"+self.type+"315.png").convert_alpha(), (178, 100))
        self.x = start[0]
        self.y = start[1]
        self.heading = 45
        self.running = False
        self.pressed = False
        self.path = Path()
    
    def draw(self, screen):
        while self.heading < 0:
            self.heading += 360
        while self.heading > 360:
            self.heading -= 360
        if self.heading < 22.5 or self.heading > 337.5:
            image = self.image0
        elif self.heading < 67.5:
            image = self.image315
        elif self.heading < 112.5:
            image = self.image270
        elif self.heading < 157.5:
            image = self.image225
        elif self.heading < 202.5:
            image = self.image180
        elif self.heading < 247.5:
            image = self.image135
        elif self.heading < 292.5:
            image = self.image90
        elif self.heading < 337.5:
            image = self.image45

        screen.blit(image, (self.x - image.get_width() / 2, self.y - image.get_height() / 2 - 10))

    def update(self, path):
        target = self.getTarget(path)
        if pygame.key.get_pressed()[self.button]:
            if not self.pressed:
                self.running = not self.running
                self.pressed = True
        else:
            self.pressed = False
        if self.running:
            if math.sqrt((target[0] - self.x) ** 2 + (target[1] - self.y) ** 2) > 2:
                self.heading = math.degrees(math.atan2(target[1] - self.y, target[0] - self.x))
                self.x += c.TRACTOR_SPEED * math.cos(math.radians(self.heading))
                self.y += c.TRACTOR_SPEED * math.sin(math.radians(self.heading))

    def getTarget(self, path):
        #get distance from tractor to target
        if len(path.path) > 0:
            target = path.toCoords()[self.path.index]
            if math.sqrt((target[0] - self.x) ** 2 + (target[1] - self.y) ** 2) < 5:
                self.path.index += 1
                if self.path.index >= len(path.path):
                    self.path.index = 0
                target = path.toCoords()[self.path.index]
        else:
            target = (self.x, self.y)
        return target
    
    def updateController(self):
        # if w key is pressed, move forward
        if pygame.key.get_pressed()[pygame.K_w]:
            self.running = True
        else:
            self.running = False
        
        # if s key is pressed, move backward
        if pygame.key.get_pressed()[pygame.K_s]:
            self.running = True
            self.y += self.speed
        else:
            self.running = False

        # if a key is pressed, turn left
        if pygame.key.get_pressed()[pygame.K_a]:
            self.running = True
            self.heading += 5
        else:
            self.running = False
        # if d key is pressed, turn right
        if pygame.key.get_pressed()[pygame.K_d]:
            self.running = True
            self.heading -= 5
        else:
            self.running = False

# tractor = pygame.image.load("images/tractor.png")
    # tractor = pygame.transform.scale(tractor, (120, 80))
    # tractor = pygame.transform.flip(tractor, True, False)
    # screen.blit(tractor, (400, 800))

class Path():
    def __init__(self):
        #make an empty array of points
        self.path = np.empty((0, 2))
        self.clicked = False
        self.selecting = True
        self.index = 0

    def toCoords(self):
        #convert the path to coordinates
        coords = []
        for point in self.path:
            coords.append(getCenterTileLocation(point))
        return coords

    def addPoint(self, x, y):
        #add a point to the path
        self.path = np.append(self.path, [[x, y]], axis=0)

    def removePoint(self):
        #remove the last point from the path
        self.path = np.delete(self.path, -1, 0)

    def draw(self, screen, tile):
        #draw the path
        if self.selecting:
            if tile[0] >= 0 and tile[0] <= 24 and tile[1] >= 0 and tile[1] <= 24:
                drawTileAlpha(screen, tile, (255, 0, 0, 100))
            if len(self.path) > 1:
                pygame.draw.lines(screen, c.WHITE, False, self.toCoords(), 2)

    def update(self, screen, mouse, click):
        tile = getClosestTile(mouse)
        if click[0] and not self.clicked:
            self.clicked = True
            if tile[0] >= 0 and tile[0] <= 24 and tile[1] >= 0 and tile[1] <= 24:
                self.addPoint(tile[0], tile[1])
        elif click[1] and not self.clicked:
            self.clicked = True
            self.removePoint()
        elif not click[0]:
            self.clicked = False
        self.draw(screen, tile)
        

