import pygame


def update():
    pass


def render(window: pygame.Surface):
    title_surface = pygame.image.load("./Assets/MainMenu/Habit pet.png").convert_alpha()
    title_rect = title_surface.get_rect()
