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

paws_left = [
    Paw("./Assets/MainMenu/Paw.png", (300, 560), False, 20),
    Paw("./Assets/MainMenu/Paw.png", (280, 380), False, 20),
    Paw("./Assets/MainMenu/Paw.png", (100, 360), False, 20),
    Paw("./Assets/MainMenu/Paw.png", (100, 200), False, 20),
]

paws_right = [
    Paw("./Assets/MainMenu/Paw.png", (980, 560), True, 20),
    Paw("./Assets/MainMenu/Paw.png", (1000, 380), True, 20),
    Paw("./Assets/MainMenu/Paw.png", (1180, 360), True, 20),
    Paw("./Assets/MainMenu/Paw.png", (1180, 200), True, 20),
]


def update():
    mouse_position = pygame.mouse.get_pos()

    dt = pygame.time.Clock().tick(60)

    for paw in paws_left:
        paw.update(dt)

    for paw in paws_right:
        paw.update(dt)

    start_backlight.update(start_button.is_hovered(mouse_position))
    options_backlight.update(options_button.is_hovered(mouse_position))
    exit_backlight.update(exit_button.is_hovered(mouse_position))


def render(window: pygame.Surface):
    for paw in paws_left:
        paw.draw(window)

    for paw in paws_right:
        paw.draw(window)

    start_backlight.draw(window)
    options_backlight.draw(window)
    exit_backlight.draw(window)

    start_button.draw(window)
    options_button.draw(window)
    exit_button.draw(window)

    window.blit(title_surf.convert_alpha(), title_rect)
