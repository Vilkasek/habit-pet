import pygame

from utils.checkboxes import Checkbox


class Task:
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        self.text = text
        self.position = position
        self.color = (255, 255, 255)

        self.font = pygame.Font(None, 50)

        self.text_surf = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surf.get_rect(topright=(self.position))

        self.checkboxes = []

        self.position_x = self.text_rect.topleft[0] + 200

        self.on_path = "./Assets/TaskMenu/Circles/CircleOn.png"
        self.off_path = "./Assets/TaskMenu/Circles/CircleOff.png"

    def create_checkboxes(self):
        if len(self.checkboxes) == 0:
            for i in range(7):
                self.checkboxes.append(
                    Checkbox(
                        self.on_path,
                        self.off_path,
                        (self.position_x, self.position[1] - 10),
                    ),
                )
                self.position_x += 60

    def handle_events(self, event: pygame.Event):
        for checkbox in self.checkboxes:
            checkbox.handle_events(event)

    def update(self):
        for checkbox in self.checkboxes:
            checkbox.update()

    def render(self, screen: pygame.Surface):
        self.text_surf = self.text_surf.convert_alpha()

        for checkbox in self.checkboxes:
            checkbox.render(screen)

        screen.blit(self.text_surf, self.text_rect)
