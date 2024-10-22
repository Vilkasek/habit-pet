import pygame

from settings import *

pygame.init()

display_surface = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Habit pet")

running = True


def event_handler() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def display():
    display_surface.fill(BACKGROUND_COLOR)

    pygame.display.update()


while running:
    running = event_handler()

    display()

pygame.quit()
