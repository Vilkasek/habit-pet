import pygame

from Utils.backlight import Backlight
from Utils.button import Button
from Utils.hint import Hint

title_surf: pygame.Surface = pygame.image.load("./Assets/TaskMenu/Your tasks.png")
title_rect: pygame.Rect = title_surf.get_rect(center=(640, 100))

backlight_path = "./Assets/TaskMenu/Controls/Backlight.png"

back_button = Button("./Assets/TaskMenu/Controls/Back.png", (80, 640))
back_hint = Hint("./Assets/TaskMenu/Tooltips/BackTooltip.png", (80, 580))
back_backlight = Backlight(backlight_path, (82, 642))

add_button = Button


def update():
    mouse_position = pygame.mouse.get_pos()

    pygame.time.Clock().tick(60)

    back_hint.update(back_button.is_hovered(mouse_position))
    back_backlight.update(back_button.is_hovered(mouse_position))


def render(window: pygame.Surface):
    back_backlight.draw(window)
    back_button.draw(window)
    back_hint.draw(window)

    window.blit(title_surf.convert_alpha(), title_rect)
