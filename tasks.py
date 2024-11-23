import pygame


class Task:
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        self.text = text
        self.position = position
        self.color = (255, 255, 255)

        self.font = pygame.Font(None, 20)

        self.text_surf = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surf.get_rect(topright=(self.position))

        self.checkboxes = []

    def update(self):
        for checkbox in self.checkboxes:
            pass

    def render(self, screen: pygame.Surface):
        self.text_surf = self.text_surf.convert_alpha()

        screen.blit(self.text_surf, self.text_rect)
