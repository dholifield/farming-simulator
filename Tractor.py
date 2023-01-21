import pygame

class Tractor():
    def __init__(self):
        self.image = pygame.image.load("images/tractor.png")
        self.x = 400
        self.y = 800
        self.heading = 45
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        pass

# tractor = pygame.image.load("images/tractor.png")
    # tractor = pygame.transform.scale(tractor, (120, 80))
    # tractor = pygame.transform.flip(tractor, True, False)
    # screen.blit(tractor, (400, 800))