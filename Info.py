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
        self.text_corn = self.font.render("Corn: " + str(c.corn_count), True, c.WHITE)
        self.text_balance = self.font.render("Balance: $%.2f" %c.balance, True, c.WHITE)
        self.text_corn_price = self.font.render("Corn Price: $%.2f" %c.CORN_PRICE, True, c.WHITE)
        self.text_seed_cost = self.font.render("Seed Cost: $%.2f" %c.SEED_COST, True, c.WHITE)
        self.sell_button = self.font.render("Sell Corn", True, c.WHITE)
        self.surface_button = pygame.Surface((125, 50))
        self.corn_index = randrange(0, len(corn_data))
        self.timer = 120
        self.past_five = []

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
        pass

    def sellCornButton(self, mouse, click):
       if click[0] == 1 and mouse[0] > self.surface_left_pos[0] + 50 and mouse[0] < self.surface_left_pos[0] + 200 and mouse[1] > self.surface_left_pos[1] + 50 and mouse[1] < self.surface_left_pos[1] + 125:  
          self.sellCorn()
          self.update() 

        