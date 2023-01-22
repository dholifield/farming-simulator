from pygame import mixer
import pygame
#from Tractor import *

class Music():
    def __init__(self):
        mixer.init()
        self.tractor_prev = False
        self.farm_song = mixer.Sound("music/Farming Song.mp3")
        self.bird = mixer.Sound("music/ambience_birds.mp3")
        self.tractor_sound = mixer.Sound("music/tractor.mp3")
        self.tractor_running = False
        self.bird_length = self.bird.get_length()
        self.timer = 60

        # code for farming song
        pygame.mixer.Channel(0).play(self.farm_song, -1)

        #volume setting for ambient birds
        pygame.mixer.Channel(1).play(self.bird, -1)
        pygame.mixer.Channel(1).set_volume(0.1)

        #volume setting for tractor
        pygame.mixer.Channel(2).set_volume(1)

    def update(self, running):
        if running and not self.tractor_running:
            pygame.mixer.Channel(2).play(self.tractor_sound, -1)
            self.tractor_running = True
        elif not running and self.tractor_running:
            pygame.mixer.Channel(2).stop()
            self.tractor_running = False