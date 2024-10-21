import pygame

pygame.init()

window_size = (1280, 720)

display_surface = pygame.display.set_mode(window_size)

pygame.display.set_caption("Habit pet")

background_color = (5, 31, 57)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.key_code("escape"):
                running = False

    display_surface.fill(background_color)

    pygame.display.update()

pygame.quit()
