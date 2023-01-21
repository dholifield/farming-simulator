class Tile():
    def __init__(self, type, price, x, y):
        self.type = type
        self.price = price
        self.x = x
        self.y = y
        self.weather = self.calculateWeather()
        self.terrain = self.calculateTerrain()

    def updatePrice(self):
        pass
    