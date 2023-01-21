from pygame import mixer
import pygame
import array as arr
import random
#from Tractor import *

class Music():
    def __init__(self):
        mixer.init()

        self.ambient1 = pygame.mixer.music.load("ambience_birds.mp3")
        self.ambient2 = pygame.mixer.music.load("ambience_tractor.mp3")

        #array for ambient sounds
        array = [self.ambient1, self.ambient2]


        #code for farming song
        #self.music = pygame.mixer.music.load("Farming Song.mp3")
        #self.music = pygame.mixer.music.play(-1)
        #self.music = pygame.mixer.music.set_volume(0.2)

        #code for random ambient sounds
        pygame.time.set_timer(random.choice(array), 10000)

        #code for tractor noise (not sure if it works, gotta check/test)
        #self.tractor = pygame.mixer.Sound("ambience_tractor.mp3")

        #while (TRACTOR MOVEMENT IS TRUE):
            #self.tractor = pygame.mixer.music.play(-1)

        #if (TRACTOR MOVEMENT IS FALSE):
            #self.tractor = pygame.mixer.music.stop()

