from random import randrange
from random import uniform
import numpy as np
from Tile import *
import pygame
import math

WIDTH = 1800
HEIGHT = 900
GREEN = (147, 216, 175)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

TILE_WIDTH = 72
TILE_HEIGHT = 36

CORN_TILE_AMOUNT =  1
SEED_COST = 1.00
CORN_PRICE = 5.00

TRACTOR_SPEED = 3
TRACTOR_SPEED_COST = 1000
GROW_SPEED = 1
GROW_SPEED_COST = 2000

corn_count = 0
balance = 100.00