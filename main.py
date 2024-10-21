import pygame

pygame.init()

window_size = (1280, 720)

display_surface = pygame.display.set_mode(window_size)

pygame.display.set_caption("Habit pet")

background_color = (5, 31, 57)

running = True


def event_handler() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def display():
    display_surface.fill(background_color)

    pygame.display.update()


while running:
    running = event_handler()

    display()

pygame.quit()
