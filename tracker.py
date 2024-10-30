import pygame

from Utils.button import Button
from Utils.hint import Hint

title_surf: pygame.Surface = pygame.image.load("./Assets/TaskMenu/Your tasks.png")
title_rect: pygame.Rect = title_surf.get_rect(center=(640, 100))

backlight_path = "./Assets/TaskMenu/Controls/Backlight.png"

back_button = Button("./Assets/TaskMenu/Controls/Back.png", (80, 640))
back_hint = Hint("./Assets/TaskMenu/Tooltips/BackTooltip.png", (80, 580))


def update():
    mouse_position = pygame.mouse.get_pos()

    back_hint.update(back_button.is_hovered(mouse_position))


def render(window: pygame.Surface):
    back_button.draw(window)
    back_hint.draw(window)

    window.blit(title_surf.convert_alpha(), title_rect)
