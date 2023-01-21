from pygame import mixer
import pygame
import array as arr

class Music():
    def __init__(self):
        self.ambient1 = pygame.mixer.music.load("ambience_birds.mp3")
        self.ambient2 = pygame.mixer.music.load("ambience_tractor.mp3")

        
        mixer.init()
        self.music = pygame.mixer.music.load("Farming Song.mp3")
        #self.music = pygame.mixer.music.play(-1)
        #self.music = pygame.mixer.music.set_volume(0.2)