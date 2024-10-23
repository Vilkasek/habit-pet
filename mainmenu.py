import pygame

title_surface: pygame.Surface
title_rect: pygame.Rect


def update():
    pass


def render(window: pygame.Surface):
    global title_surface
    global title_rect

    title_surface = pygame.image.load("./Assets/MainMenu/Habit pet.png").convert_alpha()
    title_rect = title_surface.get_rect(center=(640, 80))

    window.blit(title_surface, title_rect)
