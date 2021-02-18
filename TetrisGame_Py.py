import pygame
import math
import random
import sys
import copy
import time

from pygame.locals import *

# table
width = 12
height = 21
sqauresize = 25

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 178, 217)
PURPLE = (209, 178, 255)
SKYBLUE = (178, 235, 244)
LIGHTGREEN = (183, 240, 177)
YELLOW = (250, 237, 125)
ORANGE = (255, 193, 158)
RED = (255, 167, 167)


def drawmain(self, index, check):
    self.fill(SKYBLUE)
    fontmain = pygame.font.Font(None, 50)
    frontinfo = pygame.font.Font(None, 40)
    txtmain = fontmain.render("Welcome to Tetris", True, BLACK)
    txtstart = frontinfo.render("start game", True, BLACK)
    txtscore = frontinfo.render("score board", True, BLACK)
    txtsetting = frontinfo.render("settings", True, BLACK)
    txtend = frontinfo.render("exit", True, BLACK)
    self.blit(txtmain, (200, 50))
    self.blit(txtstart, (30, 400))
    self.blit(txtscore, (30, 430))
    self.blit(txtsetting, (30, 460))
    self.blit(txtend, (30, 490))
    if index == 0 and check:
        pygame.draw.polygon(
            self, BLACK, [[180, 415], [180+10*3**0.5, 425], [180+10*3**0.5, 405]])
    elif index == 1 and check:
        pygame.draw.polygon(
            self, BLACK, [[198, 445], [198+10*3**0.5, 455], [198+10*3**0.5, 435]])
    elif index == 2 and check:
        pygame.draw.polygon(
            self, BLACK, [[153, 475], [153+10*3**0.5, 485], [153+10*3**0.5, 465]])
    elif index == 3 and check:
        pygame.draw.polygon(
            self, BLACK, [[90, 505], [90+10*3**0.5, 515], [90+10*3**0.5, 495]])
    pygame.display.flip()


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
                        screen.fill(YELLOW)
                        pygame.display.flip()
                    elif idx == 1:
                        screen.fill(PINK)
                        pygame.display.flip()
                    elif idx == 2:
                        screen.fill(LIGHTGREEN)
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
