import pygame

import mainmenu
from settings import *

pygame.init()

display_surface = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Habit pet")

running = True


def event_handler() -> bool:
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or mainmenu.exit_button.is_clicked(
            mouse_position, event
        ):
            return False
    return True


def render():
    display_surface.fill(BACKGROUND_COLOR)

    mainmenu.render(display_surface)

    pygame.display.update()


while running:
    running = event_handler()
    render()

pygame.quit()
