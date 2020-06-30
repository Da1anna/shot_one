# -*- coding:utf-8 -*-
# @Time: 2020/6/30 16:30
# @Author: Lj
# @File: scoreboard.py

import pygame.font

class Scoreboard():

    def __init__(self, so_setting, screen):

        self.so_setting = so_setting
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #得分数
        self.score = 0

        #字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.so_setting.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.centerx = self.screen_rect.centerx

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
