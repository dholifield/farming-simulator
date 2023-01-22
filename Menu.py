import pygame
from pygame import mixer

class Menu():
    def __init__(self, screen):
        mixer.init()
        self.menu_image = pygame.image.load("images/menu.png").convert()
        self.menu_song = mixer.Sound("music/loading_screen.mp3")
        screen.blit(self.menu_image, (0,0))
        pygame.display.flip()
        self.menuMusic()

    def menuMusic(self):
        pygame.mixer.Channel(0).play(self.menu_song, -1)

    def stopMusic(self):
        pygame.mixer.music.stop()