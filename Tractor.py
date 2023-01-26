import Constants as c

class Tractor():
    def __init__(self, type, button, start):
        self.type = type
        self.button = button
        self.image0 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"0.png").convert_alpha(), (178, 100))
        self.image45 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"45.png").convert_alpha(), (178, 100))
        self.image90 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"90.png").convert_alpha(), (178, 100))
        self.image135 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"135.png").convert_alpha(), (178, 100))
        self.image180 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"180.png").convert_alpha(), (178, 100))
        self.image225 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"225.png").convert_alpha(), (178, 100))
        self.image270 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"270.png").convert_alpha(), (178, 100))
        self.image315 = c.pygame.transform.scale(c.pygame.image.load("images/"+self.type+"/"+self.type+"315.png").convert_alpha(), (178, 100))
        self.x = start[0]
        self.y = start[1]
        self.heading = 45
        self.running = False
        self.pressed = False
        self.path = Path()
        self.index = 0
    
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
        if c.pygame.key.get_pressed()[self.button]:
            if not self.pressed:
                self.running = not self.running
                self.pressed = True
        else:
            self.pressed = False
        if self.running:
            if c.math.sqrt((target[0] - self.x) ** 2 + (target[1] - self.y) ** 2) > 2:
                self.heading = c.math.degrees(c.math.atan2(target[1] - self.y, target[0] - self.x))
                self.x += c.TRACTOR_SPEED * c.math.cos(c.math.radians(self.heading))
                self.y += c.TRACTOR_SPEED * c.math.sin(c.math.radians(self.heading))

    def getTarget(self, path):
        #get distance from tractor to target
        if len(path.path) > 0:
            if self.index >= len(path.path):
                self.index = 0
            target = path.toCoords()[self.index]
            if c.math.sqrt((target[0] - self.x) ** 2 + (target[1] - self.y) ** 2) < 5:
                self.index += 1
                if self.index >= len(path.path):
                    self.index = 0
                target = path.toCoords()[self.index]
        else:
            target = (self.x, self.y)
        return target
    
    def updateController(self):
        # if w key is pressed, move forward
        if c.pygame.key.get_pressed()[c.pygame.K_w]:
            self.running = True
        else:
            self.running = False
        
        # if s key is pressed, move backward
        if c.pygame.key.get_pressed()[c.pygame.K_s]:
            self.running = True
            self.y += self.speed
        else:
            self.running = False

        # if a key is pressed, turn left
        if c.pygame.key.get_pressed()[c.pygame.K_a]:
            self.running = True
            self.heading += 5
        else:
            self.running = False
        # if d key is pressed, turn right
        if c.pygame.key.get_pressed()[c.pygame.K_d]:
            self.running = True
            self.heading -= 5
        else:
            self.running = False

class Path():
    def __init__(self):
        #make an empty array of points
        self.path = c.np.empty((0, 2))
        self.clicked = False
        self.selecting = True

    def toCoords(self):
        #convert the path to coordinates
        coords = []
        if len(self.path) > 0:
            for point in self.path:
                coords.append(c.getCenterTileLocation(point))
        return coords

    def addPoint(self, x, y):
        #add a point to the path
        self.path = c.np.append(self.path, [[x, y]], axis=0)

    def removePoint(self):
        #remove the last point from the path
        if len(self.path) > 0:
            self.path = c.np.delete(self.path, -1, 0)

    def draw(self, screen, tile):
        #draw the path
        if self.selecting:
            if tile[0] >= 0 and tile[0] <= 24 and tile[1] >= 0 and tile[1] <= 24:
                c.drawTileAlpha(screen, tile, (255, 0, 0, 100))
            if len(self.path) > 1:
                c.pygame.draw.lines(screen, c.WHITE, False, self.toCoords(), 2)

    def update(self, screen, mouse, click):
        tile = c.getClosestTile(mouse)
        if click[0] and not self.clicked:
            self.clicked = True
            if tile[0] >= 0 and tile[0] <= 24 and tile[1] >= 0 and tile[1] <= 24:
                self.addPoint(tile[0], tile[1])
        elif click[2] and not self.clicked:
            self.clicked = True
            self.removePoint()
        elif not click[0] and not click[2]:
            self.clicked = False
        self.draw(screen, tile)
        

