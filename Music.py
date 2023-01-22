from pygame import mixer
import pygame
import array as arr
import random
#from Tractor import *

class Music():
    def __init__(self):
        mixer.init()
        self.tractor_prev = False

        #self.tractor = pygame.mixer.Sound("ambience_tractor.mp3")

        self.ambient1 = pygame.mixer.music.load("ambience_birds.mp3")
        self.ambient2 = pygame.mixer.music.load("ambience_tractor_shortened.mp3")

        #array for ambient sounds
        array = [self.ambient1]


        #code for farming song
        #self.music = pygame.mixer.music.load("Farming Song.mp3")
        #self.music = pygame.mixer.music.play(-1)
        #self.music = pygame.mixer.music.set_volume(0.2)

        #code for random ambient sounds
        pygame.time.set_timer(random.choice(array), 10000)

    #def updateTractorSound(self, tractor):
        #if (tractor.running == True):
            #self.startTractor = pygame.mixer.music.subsound(0, 5000)
            #self.startTractor = pygame.mixer.music.startTractor.play()
            #self.tractor_prev = True
        #elif (tractor.running == True and self.tractor_prev == True):
            #self.tractor = pygame.mixer.music.subsound(11000, 28000)
            #self.tractor = pygame.mixer.music.tractor.play(-1)
        #else:
            #self.endTractor = pygame.mixer.music.subsound(28000, 31000)
            #self.endTractor = pygame.mixer.music.endTractor.play()
            #self.tractor_prev = False



    

