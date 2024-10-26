import pygame

from Utils.button import Button

title_surf: pygame.Surface = pygame.image.load("./Assets/MainMenu/Habit pet.png")
title_rect: pygame.Rect = title_surf.get_rect(center=(640, 100))

start_button = Button("./Assets/MainMenu/Buttons/Start.png", (640, 300))
options_button = Button("./Assets/MainMenu/Buttons/Options.png", (640, 400))
exit_button = Button("./Assets/MainMenu/Buttons/Exit.png", (640, 500))


def render(window: pygame.Surface):
    start_button.draw(window)
    options_button.draw(window)
    exit_button.draw(window)

    window.blit(title_surf.convert_alpha(), title_rect)
