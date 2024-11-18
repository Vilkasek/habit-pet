import pygame

from Utils.checkbox import Checkbox


class Task:
    def __init__(self, name, position, checkbox_paths: list):
        self.name = name
        self.position = position
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(self.name, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(topleft=position)
        self.checkboxes = [
            Checkbox((position[0] + 150 + i * 40, position[1]), checkbox_paths)
            for i in range(7)
        ]

    def draw(self, window):
        window.blit(self.text_surf, self.text_rect)
        for checkbox in self.checkboxes:
            checkbox.draw(window)

    def toggle_checkbox(self, index):
        if 0 <= index < len(self.checkboxes):
            self.checkboxes[index].toggle()
