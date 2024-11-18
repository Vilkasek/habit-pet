import pygame


class Checkbox:
    def __init__(self, position, checkbox_paths: list):
        self.image_off = pygame.image.load(checkbox_paths[0])
        self.image_on = pygame.image.load(checkbox_paths[1])
        self.rect = self.image_off.get_rect(topleft=position)
        self.checked = False

    def toggle(self):
        self.checked = not self.checked

    def draw(self, window):
        if self.checked:
            window.blit(self.image_on, self.rect)
        else:
            window.blit(self.image_off, self.rect)
