import pygame

from utils.button import Button
from utils.states import State


class TrackerMenu:
    def __init__(self, title_path: str) -> None:
        self.title_path = title_path

        self.title_surf = pygame.image.load(title_path)
        self.title_rect = self.title_surf.get_rect(center=(1280 / 2, 100))

        self.mouse_pos = (0, 0)

        self.buttons = [
            Button("./Assets/TaskMenu/Controls/Back.png", (60, 660)),
            Button("./Assets/TaskMenu/Controls/AddTaskButton.png", (640, 660)),
        ]

        self.state = State()

    def handle_events(self, event: pygame.Event):
        if self.buttons[0].is_clicked(event, self.mouse_pos):
            self.state.change_state("main-menu")
        if self.buttons[1].is_clicked(event, self.mouse_pos):
            # TODO: Taski
            pass

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def render(self, screen: pygame.Surface):
        self.title_surf.convert_alpha()

        for button in self.buttons:
            button.render(screen)

        screen.blit(self.title_surf, self.title_rect)
