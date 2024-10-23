import pygame

title_surface: pygame.Surface
title_rect: pygame.Rect

rotation_speed = 0.01
direction = 1
angle = 0
max_angle = 3


def update():
    global rotation_speed
    global angle
    global direction

    angle += rotation_speed * direction

    if angle >= max_angle or angle <= -max_angle:
        direction *= -1


def render(window: pygame.Surface):
    global title_surface
    global title_rect

    title_surface = pygame.image.load("./Assets/MainMenu/Habit pet.png").convert_alpha()
    title_surface = pygame.transform.rotate(title_surface, angle)

    title_rect = title_surface.get_rect(center=(640, 80))

    window.blit(title_surface, title_rect)
