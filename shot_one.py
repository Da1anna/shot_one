# -*- coding:utf-8 -*-
# @Time: 2020/6/27 9:56
# @Author: Lj
# @File: shot_one.py

import sys

import pygame

from settings import Setting
import game_functions as gf
from bow import Bow
from arrow import Arrow
from heart import Heart
from scoreboard import Scoreboard

def run_game():

    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    so_setting = Setting()
    pygame.display.set_caption("Shot one")

    #新建对象
    bow = Bow(so_setting, screen)
    arrow = Arrow(so_setting, screen, bow)
    heart = Heart(so_setting, screen)
    score = Scoreboard(so_setting, screen)
    #游戏的主循环
    while True:

        gf.check_events(arrow, bow)
        #更新三个对象
        gf.update_bow(bow)
        gf.update_arrow(arrow, heart, so_setting, score)
        gf.update_heart(heart)
        #更新屏幕
        gf.update_screen(screen, so_setting, bow, arrow, heart, score)
        #显示最新的屏幕
        pygame.display.flip()

run_game()