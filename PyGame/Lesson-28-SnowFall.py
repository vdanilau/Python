import pygame
import random
import sys
import time

MAX_X = 1920
MAX_Y = 1080
MAX_SNOW = 100
SNOW_SIZE = 64


class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha() # чтобы не накладывались
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:  # Move right
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:  # Move left
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(max_snow, snowfall):
    for s in range(0, MAX_SNOW):
        xx = random.randint(0, MAX_X)  # случайное начальное положение снежинки
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))


def check_for_exit():
    for even in pygame.event.get():
        if even.type == pygame.KEYDOWN:
            sys.exit()


# ------------- MAIN -------------
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []

# initialize_pygame(MAX_X, MAX_Y)

initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.020)
    pygame.display.flip()