import Constants as c

class Map():
    def __init__(self, lat, lon):
        self.tiles = c.np.zeros((25, 25))
        #make a 25x25 array of random numbers from 2000 to 3000
        self.sprout_times = c.np.zeros((25, 25))
        for i in range(0, 25):
            for j in range(0, 25):
                self.sprout_times[i][j] = c.randrange(0, 500)
        self.lat = lat
        self.lon = lon
        self.generateTerrain()
        self.grass_image = c.pygame.image.load("images/grass.png").convert_alpha()
        self.dirt_image = c.pygame.image.load("images/dirt.png").convert_alpha()
        self.rock_image = c.pygame.image.load("images/rock.png").convert_alpha()
        self.corn_image = c.pygame.image.load("images/corn.png").convert_alpha()
        self.sprout_image = c.pygame.image.load("images/sprout.png").convert_alpha()
        self.background = c.pygame.image.load("images/background.png").convert()
        self.hit_rock = False
        self.delay = 10

    def calculateWeather(self):
        pass

    def calculateTerrain(self):
        pass

    def generateTerrain(self):
        # fill everything with seeds
        for i in range(1, 24):
            for j in range(1, 24):
                self.tiles[i][j] = 4

        # randomly add 10 rocks to the map
        for i in range(0, 20):
            self.tiles[c.randrange(1, 24)][c.randrange(1, 24)] = 2

    def update(self, harvester, planter):
        for i in range (0, 25):
            for j in range (0, 25):
                if self.tiles[i][j] == 4:
                    self.sprout_times[i][j] -= c.GROW_SPEED / 2
                    if self.sprout_times[i][j] <= 0:
                        self.tiles[i][j] = 3
        harvester_tile = c.getClosestTile((harvester.x, harvester.y))
        planter_tile = c.getClosestTile((planter.x, planter.y))
        if harvester_tile[0] >= 0 and harvester_tile[0] < 25 and harvester_tile[1] >= 0 and harvester_tile[1] < 25:
            if self.tiles[harvester_tile[0]][harvester_tile[1]] == 3:
                self.tiles[harvester_tile[0]][harvester_tile[1]] = 1
                c.corn_count += c.CORN_TILE_AMOUNT
            if self.tiles[harvester_tile[0]][harvester_tile[1]] == 2 and not self.hit_rock:
                c.corn_count /= 2
                harvester.running = False
                self.hit_rock = True
            elif self.tiles[harvester_tile[0]][harvester_tile[1]] != 2 and self.hit_rock:
                self.hit_rock = False
        if planter_tile[0] >= 0 and planter_tile[0] < 25 and planter_tile[1] >= 0 and planter_tile[1] < 25:
            if self.tiles[planter_tile[0]][planter_tile[1]] == 1:
                if c.balance >= c.SEED_COST:
                    self.tiles[planter_tile[0]][planter_tile[1]] = 4
                    c.balance -= c.SEED_COST
                    self.sprout_times[planter_tile[0]][planter_tile[1]] = c.randrange(50, 60) * 60
                else:
                    planter.running = False

    def draw(self, screen):
        for i in range(0, 25):
            for j in range(0, 25):
                if self.tiles[i][j] == 0:
                    c.drawImageTile(screen, (i, j), self.grass_image)
                elif self.tiles[i][j] == 1:
                    c.drawImageTile(screen, (i, j), self.dirt_image)
                elif self.tiles[i][j] == 2:
                    c.drawImageTile(screen, (i, j), self.rock_image)
                elif self.tiles[i][j] == 3:
                    c.drawImageTile(screen, (i, j), self.corn_image)
                elif self.tiles[i][j] == 4:
                    c.drawImageTile(screen, (i, j), self.sprout_image)
                if self.delay > 0:
                        c.pygame.time.delay(self.delay)
                        c.pygame.display.flip()
        self.delay = 0

    def drawBackground(self, screen):
        screen.blit(self.background, (0, 0))
    
    def generateBackrgound(self, screen):
           # generate background image
            for i in range(0, 13):
                for j in range(-7, 0):
                    c.drawBigImageTile(screen, (2*j, 2*i), c.pygame.image.load("images/tree.png"))
                    c.drawBigImageTile(screen, (2*i, 2*j), c.pygame.image.load("images/tree.png"))

            for i in range(0, 25):
                for j in range(25, 40):
                    c.drawImageTile(screen, (i, j), c.pygame.image.load("images/grass.png"))
                    c.drawImageTile(screen, (j, i), c.pygame.image.load("images/water.png"))

            for i in range (0, 25):
                c.drawImageTile(screen, (25, i), c.pygame.image.load("images/grass.png"))
                c.drawImageTile(screen, (26, i), c.pygame.image.load("images/grass.png"))
                c.drawImageTile(screen, (27, i), c.pygame.image.load("images/dirt.png"))

            barn = c.pygame.image.load("images/barn.png")
            barn = c.pygame.transform.scale(barn, (400, 350))
            screen.blit(barn, (5, 550))
