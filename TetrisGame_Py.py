import pygame
import math
import random
import sys
import copy
import time

from pygame.locals import *

# now point
now_x = 4
now_y = 0

# block info
nowblock = 0
nxtblock = 0
blockvector = 0

# table
width = 12
height = 23
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
for i in range(2, height):
    table[i][0] = 1
    table[i][11] = 1
for i in range(width):
    table[22][i] = 1
    table[1][i] = 1

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

start_time = pygame.time.get_ticks()
start_ground_time = pygame.time.get_ticks()
end_time = pygame.time.get_ticks()

score = 0
level = 0


def findcolor(tmp):
    if tmp == 1:
        tmp_color = "WHITE"
    elif tmp == 2:
        tmp_color = "PINK"
    elif tmp == 3:
        tmp_color = "PURPLE"
    elif tmp == 4:
        tmp_color = "SKYBLUE"
    elif tmp == 5:
        tmp_color = "LIGHTGREEN"
    elif tmp == 6:
        tmp_color = "YELLOW"
    elif tmp == 7:
        tmp_color = "ORANGE"
    elif tmp == 8:
        tmp_color = "RED"
    return tmp_color


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


def check(x, y):
    global nowblock
    global blockvector
    for i in range(4):
        for j in range(4):
            if block[nowblock][blockvector][i][j]:
                tmp = table[y+i][x+j]
                if tmp:
                    return 0
    return 1


def gamestop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def dropblock(self):
    global start_time
    global start_ground_time
    global end_time
    global now_x
    global now_y
    global level
    end_time = pygame.time.get_ticks()
    if end_time-start_time >= 800-500*(1-0.995**(level//10)):
        if check(now_x, now_y+1):
            now_y += 1
            start_time = pygame.time.get_ticks()
            start_ground_time = pygame.time.get_ticks()
            drawtable(self)
            drawblock(self)


def blocktoground(self):
    global now_x
    global now_y
    global start_ground_time
    global end_time
    global nowblock
    global blockvector
    if check(now_x, now_y+1) == 0:
        if end_time-start_ground_time >= 800:
            for i in range(4):
                for j in range(4):
                    if block[nowblock][blockvector][i][j]:
                        table[now_y+i][now_x+j] = nowblock+2
            now_x = 4
            now_y = 0
            blockvector = 0
            randomblock()
            drawtable(self)
            drawblock(self)


def drawtable(self):
    global nxtblock
    global score
    global level
    self.fill(color["BLACK"])
    for i in range(height):
        for j in range(width):
            if table[i][j]:
                tmp_color = findcolor(table[i][j])
                pygame.draw.rect(self, color[tmp_color], [
                                 100+j*20, 120+i*20, 20, 20])
    pygame.draw.rect(self, color["WHITE"], [100, 140, 340, 20])
    pygame.draw.rect(self, color["WHITE"], [340, 160, 100, 20])
    pygame.draw.rect(self, color["WHITE"], [340, 260, 100, 320])
    pygame.draw.rect(self, color["WHITE"], [420, 180, 20, 80])
    for i in range(4):
        for j in range(4):
            if block[nxtblock][0][i][j]:
                tmp_color = findcolor(nxtblock+2)
                pygame.draw.rect(self, color[tmp_color], [
                                 340+j*20, 180+i*20, 20, 20])
    txtfont = pygame.font.Font(None, 20)
    txtscore = txtfont.render("SCORE : ", True, color["BLACK"])
    txtlevel = txtfont.render("LEVEL : ", True, color["BLACK"])
    self.blit(txtscore, (325, 300))
    self.blit(txtlevel, (325, 310))
    pygame.display.flip()


def drawblock(self):
    global now_x
    global now_y
    global nowblock
    global blockvector
    for i in range(4):
        for j in range(4):
            if block[nowblock][blockvector][i][j] == 1:
                tmp_color = findcolor(nowblock+2)
                pygame.draw.rect(self, color[tmp_color], [
                                 100+now_x*20+j*20, 120+now_y*20+i*20, 20, 20])
    pygame.display.update()


def randomblock():
    global nowblock
    global nxtblock
    nowblock = nxtblock
    nxtblock = random.randrange(7)


def removeline(self):
    global height
    global width
    global score
    global level
    count = 0
    for i in range(2, height-1):
        chk = 1
        for j in range(1, width-1):
            if table[i][j] == 0:
                chk = 0
                break
        if chk:
            count += 1
            for j in range(i, 1, -1):
                for k in range(1, width-1):
                    if j != 2:
                        table[j][k] = table[j-1][k]
                    else:
                        table[j][k] = 0
    score += 100*count*count
    level += count*count
    if count:
        drawtable(self)
        drawblock(self)


def space_bar():
    global now_x
    global now_y
    while True:
        if check(now_x, now_y+1):
            now_y += 1
        else:
            break


def checkgameend():
    global now_y
    global now_x
    global nowblock
    if now_x == 4 and now_y == 0:
        for i in range(4):
            for j in range(4):
                if block[nowblock][0][i][j]:
                    if table[now_y+i][now_x+j]:
                        return 1
    return 0


def startgame(self):
    run = True
    global width
    global height
    global nxtblock
    global start_time
    global blockvector
    global now_x
    global now_y
    start_time = pygame.time.get_ticks()
    nxtblock = random.randrange(7)
    randomblock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestop()
                if event.key == pygame.K_UP:
                    blockvector = (blockvector+1) % 4
                    if check(now_x, now_y) == 0:
                        blockvector = (blockvector-1) % 4
                    drawtable(self)
                    drawblock(self)
                if event.key == pygame.K_DOWN:
                    blockvector = (blockvector-1) % 4
                    if check(now_x, now_y) == 0:
                        blockvector = (blockvector+1) % 4
                    drawtable(self)
                    drawblock(self)
                if event.key == pygame.K_LEFT:
                    if check(now_x-1, now_y):
                        now_x -= 1
                        drawtable(self)
                        drawblock(self)
                if event.key == pygame.K_RIGHT:
                    if check(now_x+1, now_y):
                        now_x += 1
                        drawtable(self)
                        drawblock(self)
                if event.key == pygame.K_SPACE:
                    space_bar()
        dropblock(self)
        blocktoground(self)
        if checkgameend():
            run = False
            for i in range(2, height-1):
                for j in range(1, width-1):
                    table[i][j] = 0
            break
        removeline(self)


def initgame():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Tetris")
    global start_time
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
