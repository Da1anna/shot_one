# -*- coding:utf-8 -*-
# @Time: 2020/6/27 10:22
# @Author: Lj
# @File: game_functions.py


import sys
import pygame


def update_screen(screen, so_setting, bow, arrow, heart, score):
    """更新屏幕上的元素"""
    screen.fill(so_setting.bg_color)
    bow.blitme()
    arrow.blitme()
    heart.blitme()
    score.show_score()

def update_bow(bow):
    """更新弓的位置"""
    bow.pos_update()

def update_arrow(arrow, heart, so_setting, score):
    """更新箭的位置"""

    # 箭发射前更新位置
    _arrow_before_loose(arrow)

    # 箭发射后更新位置
    _arrow_after_loose(arrow)

    #检测碰撞
    _check_collision(arrow, heart, so_setting, score)

    # 箭到达屏幕边缘后更新位置
    _check_arrow_edge(arrow)

def update_heart(heart):
    """"""
    heart.pos_update()

    _check_heart_edge(heart)

def check_events(arrow, bow):
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            _check_keydown_events(arrow, event, bow)
        if event.type == pygame.KEYUP:
            _check_keyup_events(event, bow)

def _check_collision(arrow, heart, so_setting, score):
    """检测箭和心的碰撞"""
    if pygame.sprite.collide_rect(arrow, heart):
        arrow.initialize_pos()
        heart.initialize_pos()
        so_setting.heart_speedup()
        score.score += 1
        score.prep_score()

def _check_keyup_events(event, bow):
    """检测松开键"""
    if event.key == pygame.K_UP:
        bow.moving_up = False
    elif event.key == pygame.K_DOWN:
        bow.moving_down = False

def _check_keydown_events(arrow, event, bow):
    """检测按下键"""
    if event.key == pygame.K_UP:
        bow.moving_up = True
    elif event.key == pygame.K_DOWN:
        bow.moving_down = True
    elif event.key == pygame.K_SPACE:
        _loosed(arrow)
    elif event.key == pygame.K_q:
        sys.exit()

def _loosed(arrow):
    """射箭"""
    arrow.loosed = True

def _arrow_before_loose(arrow):
    """箭发射前的位置更新"""
    if not arrow.loosed:
        arrow.initialize_pos()

def _arrow_after_loose(arrow):
    if arrow.loosed:
        arrow.pos_update()

def _check_arrow_edge(arrow):
    """检测箭是否到达屏幕边界"""
    if arrow.rect.left >= arrow.screen_rect.right:
        #箭回到弓的位置，并重设loosed
        arrow.initialize_pos()
        arrow.loosed = False

def _check_heart_edge(heart):
    """检测心是否到达屏幕底端"""

    if heart.rect.top >= heart.screen_rect.bottom:
        heart.initialize_pos()
