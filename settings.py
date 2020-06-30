# -*- coding:utf-8 -*-
# @Time: 2020/6/27 10:16
# @Author: Lj
# @File: settings.py

class Setting():

    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #箭的设置
        self.arrow_speed = 5

        #心的设置
        self.heart_drop_speed = 0.5
        self.speedup_scale = 1.1

    def heart_speedup(self):
        self.heart_drop_speed *= self.speedup_scale