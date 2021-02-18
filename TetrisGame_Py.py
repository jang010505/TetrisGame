import pygame
import math
import random
import sys
import copy
import time

from pygame.locals import *

# now point
now_x = 120
now_y = 140

# block tmp
nowblock = 0
nxtblock = 0

# table
width = 12
height = 21
sqauresize = 25

# color
color = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "PINK": (255, 178, 217),
    "PURPLE": (209, 178, 255),
    "SKYBLUE": (178, 235, 244),
    "LIGHTGREEN": (183, 240, 177),
    "YELLOW": (250, 237, 125),
    "ORANGE": (255, 193, 158),
    "RED": (255, 167, 167)}

# table
table = [[0]*width for i in range(height)]
for i in range(height):
    table[i][0] = 1
    table[i][11] = 1
for i in range(width):
    table[20][i] = 1

# block
block = list()
for i in range(7):
    block.append([])
# block 1
block[0].append([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
block[0].append([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]])
block[0].append([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]])
block[0].append([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]])
# block 2
block[1].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
block[1].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
block[1].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
block[1].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
# block 3
block[2].append([[0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]])
block[2].append([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
block[2].append([[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]])
block[2].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]])
# block 4
block[3].append([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]])
block[3].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0]])
block[3].append([[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
block[3].append([[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
# block 5
block[4].append([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0]])
block[4].append([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]])
block[4].append([[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]])
block[4].append([[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
# block 6
block[5].append([[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
block[5].append([[0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
block[5].append([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0]])
block[5].append([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]])
# block 7
block[6].append([[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0]])
block[6].append([[0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
block[6].append([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0]])
block[6].append([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]])


def drawmain(self, index, check):
    self.fill(color["SKYBLUE"])
    fontmain = pygame.font.Font(None, 50)
    frontinfo = pygame.font.Font(None, 40)
    txtmain = fontmain.render("Welcome to Tetris", True, color["BLACK"])
    txtstart = frontinfo.render("start game", True, color["BLACK"])
    txtscore = frontinfo.render("score board", True, color["BLACK"])
    txtsetting = frontinfo.render("settings", True, color["BLACK"])
    txtend = frontinfo.render("exit", True, color["BLACK"])
    self.blit(txtmain, (200, 50))
    self.blit(txtstart, (30, 400))
    self.blit(txtscore, (30, 430))
    self.blit(txtsetting, (30, 460))
    self.blit(txtend, (30, 490))
    if index == 0 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[180, 415], [180+10*3**0.5, 425], [180+10*3**0.5, 405]])
    elif index == 1 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[198, 445], [198+10*3**0.5, 455], [198+10*3**0.5, 435]])
    elif index == 2 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[153, 475], [153+10*3**0.5, 485], [153+10*3**0.5, 465]])
    elif index == 3 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[90, 505], [90+10*3**0.5, 515], [90+10*3**0.5, 495]])
    pygame.display.flip()


def gamestop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def drawtable(self):
    self.fill(color["BLACK"])
    for i in range(height):
        for j in range(width):
            if table[i][j]:
                if table[i][j] == 1:
                    tmp_color = "WHITE"
                elif table[i][j] == 2:
                    tmp_color = "PINK"
                elif table[i][j] == 3:
                    tmp_color = "PURPLE"
                elif table[i][j] == 4:
                    tmp_color = "SKYBLUE"
                elif table[i][j] == 5:
                    tmp_color = "LIGHTGREEN"
                elif table[i][j] == 6:
                    tmp_color = "YELLOW"
                elif table[i][j] == 7:
                    tmp_color = "RED"
                pygame.draw.rect(self, color[tmp_color], [
                                 100+j*20, 120+i*20, 20, 20])
    pygame.display.flip()


def drawblock():
    global now_x
    global now_y
    global nowblock
    for i in range(4):
        for j in range(4):
            x = 1


def randomblock():
    global nowblock
    global nxtblock
    nowblock = nxtblock
    nxtblock = random.randrange(7)


def startgame(self):
    run = True
    global nxtblock
    nxtblock = random.randrange(7)
    randomblock()
    drawtable(self)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestop()
        drawblock()


def initgame():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Tetris")
    idx = 0
    check = 0
    run = True
    start_time = pygame.time.get_ticks()
    while run:
        tmp_time = pygame.time.get_ticks()
        if tmp_time-start_time >= 600:
            start_time = tmp_time
            check = abs(check-1)
            drawmain(screen, idx, check)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if idx == 0:
                        startgame(screen)
                        check = 1
                        start_time = pygame.time.get_ticks()
                        drawmain(screen, idx, check)
                    elif idx == 1:
                        screen.fill(color["PINK"])
                        pygame.display.flip()
                    elif idx == 2:
                        screen.fill(color["LIGHTGREEN"])
                        pygame.display.flip()
                    elif idx == 3:
                        run = False
                elif event.key == pygame.K_UP:
                    idx -= 1
                    idx %= 4
                    check = 1
                    start_time = pygame.time.get_ticks()
                    drawmain(screen, idx, check)
                elif event.key == pygame.K_DOWN:
                    idx += 1
                    idx %= 4
                    check = 1
                    start_time = pygame.time.get_ticks()
                    drawmain(screen, idx, check)


initgame()
pygame.quit()
