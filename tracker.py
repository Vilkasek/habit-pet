import pygame

from Utils.button import Button

title_surf: pygame.Surface = pygame.image.load("./Assets/TaskMenu/Your tasks.png")
title_rect: pygame.Rect = title_surf.get_rect(center=(640, 100))


def render(window: pygame.Surface):
    window.blit(title_surf.convert_alpha(), title_rect)
