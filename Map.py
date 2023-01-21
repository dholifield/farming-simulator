import numpy as np

class Map():
    def __init__(self, lat, lon):
        self.tiles = np.zeros((25, 25))
        self.lat = lat
        self.lon = lon

    def calculateWeather(self):
        pass

    def calculateTerrain(self):
        pass