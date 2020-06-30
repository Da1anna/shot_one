# -*- coding:utf-8 -*-
# @Time: 2020/6/29 10:37
# @Author: Lj
# @File: heart.py


import pygame
from pygame.sprite import Sprite

class Heart(Sprite):

    def __init__(self, so_setting, screen):
        super().__init__()

        self.so_setting = so_setting
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #基础属性
        self.image = pygame.image.load('images/heart.png')
        self.image = pygame.transform.scale(self.image, (80, 80))  # 缩小图片尺寸
        self.image.set_colorkey((255, 255, 255))  # 将弓的背景色设为透明
        self.rect = self.image.get_rect()
        self.initialize_pos()

    def blitme(self):
        """在屏幕上显示"""
        self.screen.blit(self.image, self.rect)

    def pos_update(self):
        """位置更新"""
        if self.rect.top < self.screen_rect.bottom:
            self.y += self.so_setting.heart_drop_speed
            self.rect.top = self.y

    def initialize_pos(self):
        """初始化心的位置：屏幕右上角"""
        self.rect.bottom = 0
        self.rect.right = self.screen_rect.right
        self.y = float(self.rect.top)

