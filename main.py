import pygame

import mainmenu
import tracker
from settings import *

pygame.init()

display_surface = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Habit pet")

running = True

states = ["MainMenu", "Options", "Tracker"]
state = states[0]


def event_handler() -> bool:
    global state

    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or mainmenu.exit_button.is_clicked(
            mouse_position, event
        ):
            return False
        if mainmenu.start_button.is_clicked(mouse_position, event):
            state = states[2]
    return True


def render():
    display_surface.fill(BACKGROUND_COLOR)

    match state:
        case "MainMenu":
            mainmenu.render(display_surface)
        case "Tracker":
            tracker.render(display_surface)
        case "Options":
            pass

    pygame.display.update()


while running:
    running = event_handler()
    render()

pygame.quit()
