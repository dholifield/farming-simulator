import pygame
import Constants as c
from random import randrange

fid = open("corn_prices.txt", "r")
corn_data = fid.readlines()
fid.close()

class Info():
    def __init__(self):
        self.corn_logo = pygame.transform.scale(pygame.image.load("images/corn_icon.png").convert_alpha(), (75, 75))
        self.coin_logo = pygame.transform.scale(pygame.image.load("images/coin.png").convert_alpha(), (62,62))
        #self.bank_logo = pygame.image.load("images/tractor270.png").convert_alpha()
        self.font = pygame.font.Font("consolas.ttf", 20)
        self.font2 = pygame.font.Font("consolas.ttf", 15)
        self.text_corn = self.font.render("Corn: " + str(c.corn_count), True, c.WHITE)
        self.text_balance = self.font.render("Balance: $%.2f" %c.balance, True, c.WHITE)
        self.text_corn_price = self.font.render("Corn Price: $%.2f" %c.CORN_PRICE, True, c.WHITE)
        self.text_seed_cost = self.font.render("Seed Cost: $%.2f" %c.SEED_COST, True, c.WHITE)
        self.sell_button = self.font.render("Sell Corn", True, c.WHITE)
        self.surface_button = pygame.Surface((125, 50))
        self.corn_index = randrange(0, len(corn_data))
        self.timer = 120
        self.past_five = []

        self.speed_button = self.font2.render("Upgrade Speed [3] [$1000]", True, c.WHITE)
        self.surface_speed_button = pygame.Surface((220, 30))
        self.speed_button_clicked = False

        self.yield_button = self.font2.render("Upgrade Growing [1] [$2500]", True, c.WHITE)
        self.surface_yield_button = pygame.Surface((235, 30))
        self.yield_button_clicked = False

    def updateCornPrice(self): #add update later
        if self.timer == 0:
            self.corn_index = randrange(0, len(corn_data))
            if self.corn_index >= len(corn_data):
                self.corn_index = 0
            self.timer = 120

            c.CORN_PRICE = float(corn_data[self.corn_index])
            c.SEED_COST = c.CORN_PRICE / 5

            self.past_five.append(c.CORN_PRICE)
            if len(self.past_five) > 5:
                self.past_five.pop(0)
        else:
            self.timer -= 1
        

    def showGraph(self, screen):
        points = []
        for i in range(len(self.past_five)):
            points.append((i * 62 + 50, 50 - self.past_five[i] * 5))
        if len(points) > 1:
            pygame.draw.lines(screen, c.WHITE, False, points, 2)

    def sellCorn(self):
        c.balance += c.corn_count * c.CORN_PRICE
        c.corn_count = 0

    def update(self):
        self.text_corn = self.font.render("Bushels of Corn: " + str(int(c.corn_count)), True, c.WHITE)
        self.text_balance = self.font.render("Balance: $%.2f" %c.balance, True, c.WHITE)
        self.text_corn_price = self.font.render("Bushel Price: $%.2f" %c.CORN_PRICE, True, c.WHITE)
        self.text_seed_cost = self.font.render("Seed Cost: $%.2f" %c.SEED_COST, True, c.WHITE)

    def draw(self, screen):
        self.surface_left = pygame.Surface((250, 150), pygame.SRCALPHA)
        self.surface_right = pygame.Surface((250, 150), pygame.SRCALPHA)

        self.surface_left.fill(c.BLACK)
        self.surface_right.fill(c.BLACK)

        self.surface_left_pos = [50, 50]
        self.surface_right_pos = [(c.WIDTH/2) + 600, 50]

        self.surface_left.set_alpha(150)
        self.surface_right.set_alpha(150)

        screen.blit(self.surface_left, self.surface_left_pos)
        screen.blit(self.surface_right, self.surface_right_pos)

        self.sell_text = self.font.render("Sell Corn", True, c.WHITE)
        screen.blit(self.corn_logo, (c.WIDTH - 380, 50))
        screen.blit(self.coin_logo, (c.WIDTH - 373, 132))
        #screen.blit(self.bank_logo, LOCATION MATH (To do))

        screen.blit(self.text_corn, ((self.surface_right_pos[0] + 25), (self.surface_right_pos[1] + 33)))
        screen.blit(self.text_balance, ((self.surface_right_pos[0] + 25), (self.surface_right_pos[1] + 100)))
        screen.blit(self.text_corn_price, ((self.surface_left_pos[0] + 25), (self.surface_left_pos[1] + 15)))
        screen.blit(self.text_seed_cost, ((self.surface_left_pos[0] + 25), (self.surface_left_pos[1] + 50)))

        #sell button
        self.surface_button.fill(c.GRAY)
        screen.blit(self.surface_button, (self.surface_left_pos[0] + 65, self.surface_left_pos[1] + 83))
        screen.blit(self.sell_text, (self.surface_left_pos[0] + 79, self.surface_left_pos[1] + 100))

        #speed button
        self.surface_speed_button.fill(c.GRAY)
        screen.blit(self.surface_speed_button, (500, c.HEIGHT-35))
        screen.blit(self.speed_button, (510, c.HEIGHT-28))

        #yield button
        self.surface_yield_button.fill(c.GRAY)
        screen.blit(self.surface_yield_button, (250, c.HEIGHT-35))
        screen.blit(self.yield_button, (260, c.HEIGHT-28))

    def sellCornButton(self, mouse, click):
        if click[0] == 1 and mouse[0] > self.surface_left_pos[0] + 50 and mouse[0] < self.surface_left_pos[0] + 200 and mouse[1] > self.surface_left_pos[1] + 50 and mouse[1] < self.surface_left_pos[1] + 125:  
          self.sellCorn()

    def speedButton(self, mouse, click):
        if click[0] == 1 and mouse[0] > 500 and mouse[0] < 720 and mouse[1] > c.HEIGHT-35 and mouse[1] < c.HEIGHT-5:
            if not self.speed_button_clicked:
                if c.balance >= c.TRACTOR_SPEED_COST and c.TRACTOR_SPEED < 10:
                    c.TRACTOR_SPEED += 1
                    c.balance -= c.TRACTOR_SPEED_COST
                    c.TRACTOR_SPEED_COST *= 1.5
                    self.speed_button = self.font2.render("Upgrade Speed ["+str(c.TRACTOR_SPEED)+"] [$"+str(int(c.TRACTOR_SPEED_COST))+"]", True, c.WHITE)
                if c.TRACTOR_SPEED == 10:
                    self.speed_button = self.font2.render("Upgrade Speed ["+str(c.TRACTOR_SPEED)+"] [MAX]", True, c.WHITE)
                self.speed_button_clicked = True
        else:
            self.speed_button_clicked = False

    def yieldButton(self, mouse, click):
        if click[0] == 1 and mouse[0] > 250 and mouse[0] < 485 and mouse[1] > c.HEIGHT-35 and mouse[1] < c.HEIGHT-5:
            if not self.yield_button_clicked:
                if c.balance >= c.GROW_SPEED_COST and c.GROW_SPEED < 5:
                    c.GROW_SPEED += 1
                    c.balance -= c.GROW_SPEED_COST
                    c.GROW_SPEED_COST *= 1.5
                    self.yield_button = self.font2.render("Upgrade Growing ["+str(c.GROW_SPEED)+"] [$"+str(int(c.GROW_SPEED_COST))+"]", True, c.WHITE)
                if c.GROW_SPEED == 5:
                    self.yield_button = self.font2.render("Upgrade Growing ["+str(c.GROW_SPEED)+"] [MAX]", True, c.WHITE)
                self.yield_button_clicked = True
        else:
            self.yield_button_clicked = False

        