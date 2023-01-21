class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.content = None #can be barn or any type of crop
        self.weather = self.calculateWeather()
        self.terrain = self.calculateTerrain()

    def calculateWeather(self):
        pass

    def calculateTerrain(self):
        pass