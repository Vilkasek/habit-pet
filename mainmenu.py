import pygame

from Utils.backlight import Backlight
from Utils.button import Button
from Utils.paws import Paw

title_surf: pygame.Surface = pygame.image.load("./Assets/MainMenu/Habit pet.png")
title_rect: pygame.Rect = title_surf.get_rect(center=(640, 100))

backlight_path = "./Assets/MainMenu/Buttons/Backlight.png"

start_backlight = Backlight(backlight_path, (638, 299))
options_backlight = Backlight(backlight_path, (638, 399))
exit_backlight = Backlight(backlight_path, (638, 499))

start_button = Button("./Assets/MainMenu/Buttons/Start.png", (640, 300))
options_button = Button("./Assets/MainMenu/Buttons/Options.png", (640, 400))
exit_button = Button("./Assets/MainMenu/Buttons/Exit.png", (640, 500))

paws_path = "./Assets/MainMenu/Paw_Animation/"
paws = [Paw(paws_path, (300, 500), 1, False), Paw(paws_path, (1000, 300), 1, True)]


def update():
    mouse_position = pygame.mouse.get_pos()

    start_backlight.update(start_button.is_hovered(mouse_position))
    options_backlight.update(options_button.is_hovered(mouse_position))
    exit_backlight.update(exit_button.is_hovered(mouse_position))

    for paw in paws:
        paw.update()


def render(window: pygame.Surface):
    for paw in paws:
        paw.draw(window)

    start_backlight.draw(window)
    options_backlight.draw(window)
    exit_backlight.draw(window)

    start_button.draw(window)
    options_button.draw(window)
    exit_button.draw(window)

    window.blit(title_surf.convert_alpha(), title_rect)
