from time import sleep, time
import Constants as c
import Music
from Map import *
from Tractor import *
from Info import *
from Particles import *

def main():
    c.pygame.init()
    Music.init()
    Music.playMenu()
    c.pygame.display.set_caption("Farming Simulator")
    screen = c.pygame.display.set_mode((c.WIDTH, c.HEIGHT))

    # menu screen
    screen.blit(c.pygame.image.load("images/menu.png").convert(), (0,0))
    c.pygame.display.flip()   

    # wait until a button is pressed
    while 1:
        for event in c.pygame.event.get():
            if event.type == c.pygame.QUIT:
                return

        keys = c.pygame.key.get_pressed()
        if any(keys):
            break
    # end while

    # create the map
    map = Map(0, 0)
    map.drawBackground(screen)
    map.draw(screen)

    # update music
    Music.playGame()

    # create the tractors
    harvester = Tractor("harvester", c.pygame.K_1, (520, 780))
    planter = Tractor("planter", c.pygame.K_2, (450, 820))
    path = Path()
    info = Info()
    fertilizer_particles = ParticleSystem(c.WHITE)

    c.pygame.display.flip()

    while 1:
        t0 = time()

        # stop the game if the user closes the window
        for event in c.pygame.event.get():
            if event.type == c.pygame.QUIT:
                return

        mouse = c.pygame.mouse.get_pos()
        click = c.pygame.mouse.get_pressed()

        map.drawBackground(screen)
        map.update(harvester, planter)
        map.draw(screen)

        path.update(screen, mouse, click)

        if planter.running:
            fertilizer_particles.spawn_particle(planter.x, planter.y)
        fertilizer_particles.update()
        fertilizer_particles.draw(screen)

        harvester.update(path)
        harvester.draw(screen)

        planter.update(path)
        planter.draw(screen)

        info.updateCornPrice()
        info.speedButton(mouse, click)
        info.yieldButton(mouse, click)
        info.sellCornButton(mouse, click)
        info.update()
        info.draw(screen)
        info.showGraph(screen)

        Music.update(harvester.running or planter.running)

        c.pygame.display.flip()

        tf = time()

        dt = tf - t0
        if dt < 1/60:
            sleep(1/60 - dt)
        #print(1/dt)
    # end while

if __name__ == "__main__":
    main()
    