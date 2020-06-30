# -*- coding:utf-8 -*-
# @Time: 2020/6/27 15:53
# @Author: Lj
# @File: arrow.py

import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):

    def __init__(self,so_setting, screen, bow):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.so_setting = so_setting
        self.bow = bow

        #箭的基础属性
        self.image = pygame.image.load('images/arrow1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))  # 缩小图片尺寸
        self.image = pygame.transform.rotate(self.image,90)
        self.image.set_colorkey((255, 255, 255))  # 将弓的背景色设为透明
        self.rect = self.image.get_rect()
        self.initialize_pos()

        #发射与否标志
        self.loosed = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def pos_update(self):
        if self.rect.left < self.screen_rect.width:
            self.rect.left += self.so_setting.arrow_speed

    def initialize_pos(self):
        """初始化箭的位置：在当前弓的位置"""
        self.rect.right = self.bow.rect.right
        self.rect.centery = self.bow.rect.centery
        self.loosed = False