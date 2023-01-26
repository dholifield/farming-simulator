from pygame import mixer

mixer.init()
menu_song = mixer.Sound("music/loading_screen.mp3")
farm_song = mixer.Sound("music/Farming Song.mp3")
bird = mixer.Sound("music/ambience_birds.mp3")
tractor_sound = mixer.Sound("music/tractor.mp3")
tractor_running = False

# initialize the mixer
def init():
    #volume setting for main music
    mixer.Channel(0).set_volume(0.3)

    #volume setting for ambient birds
    mixer.Channel(1).play(bird, -1)
    mixer.Channel(1).set_volume(0.1)

    #volume setting for tractor
    mixer.Channel(2).set_volume(0.3)

# play the menu music
def playMenu():
    mixer.Channel(0).stop()
    mixer.Channel(0).play(menu_song, -1)

# play the game music
def playGame():
    mixer.Channel(0).stop()
    mixer.Channel(0).play(farm_song, -1)

# play the tractor sound
def update(running):
    global tractor_running
    if running and not tractor_running:
        mixer.Channel(2).play(tractor_sound, -1)
        tractor_running = True
    elif not running and tractor_running:
        mixer.Channel(2).stop()
        tractor_running = False