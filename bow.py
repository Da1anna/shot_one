# -*- coding:utf-8 -*-
# @Time: 2020/6/27 10:40
# @Author: Lj
# @File: bow.py

import pygame

class Bow():

    def __init__(self, so_setting, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        #弓的基础属性
        self.image = pygame.image.load('images/bow1.png')
        self.image = pygame.transform.scale(self.image,(70,70))     #缩小图片尺寸
        self.image.set_colorkey((255,255,255))       #将弓的背景色设为透明
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.centery = self.screen_rect.centery
        # self.y = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        #在屏幕上显示弓
        self.screen.blit(self.image, self.rect)

    def pos_update(self):
        """移动弓"""
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
