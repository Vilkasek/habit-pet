import pygame

title_surf: pygame.Surface
title_rect: pygame.Rect

start_button_surf: pygame.Surface
start_button_rect: pygame.Rect

options_button_surf: pygame.Surface
options_button_rect: pygame.Rect

exit_button_surf: pygame.Surface
exit_button_rect: pygame.Rect


def update():
    pass


def render(window: pygame.Surface):
    global title_surf, title_rect
    global start_button_surf, start_button_rect
    global options_button_surf, options_button_rect
    global exit_button_surf, exit_button_rect

    title_surf = pygame.image.load("./Assets/MainMenu/Habit pet.png").convert_alpha()
    title_rect = title_surf.get_rect(center=(640, 100))

    start_button_surf = pygame.image.load(
        "./Assets/MainMenu/Buttons/Start.png"
    ).convert_alpha()
    start_button_rect = start_button_surf.get_rect(center=(640, 300))

    options_button_surf = pygame.image.load(
        "./Assets/MainMenu/Buttons/Options.png"
    ).convert_alpha()
    options_button_rect = options_button_surf.get_rect(center=(640, 380))

    exit_button_surf = pygame.image.load(
        "./Assets/MainMenu/Buttons/Exit.png"
    ).convert_alpha()
    exit_button_rect = exit_button_surf.get_rect(center=(640, 460))

    window.blit(title_surf, title_rect)
    window.blit(start_button_surf, start_button_rect)
    window.blit(options_button_surf, options_button_rect)
    window.blit(exit_button_surf, exit_button_rect)
