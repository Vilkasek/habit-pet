import pygame

from utils.button import Button
from utils.states import State

class Petroom:
    def __init__(self, path: str) -> None:
        self.p_img: pygame.Surface = pygame.image.load(path)
        self.p_rect = self.p_img.get_rect(center=(640,360))

        self.state = State()

        self.back_button = Button("./Assets/TaskMenu/Controls/Back.png", (64, 680))

    def handle_events(self, event: pygame.Event):
        mouse_pos = pygame.mouse.get_pos()

        if self.back_button.is_clicked(event, mouse_pos):
            self.state.change_state("tracker")

    def update(self) -> None:
        pass

    def render(self, window: pygame.Surface) -> None:
        self.p_img = self.p_img.convert_alpha()
        
        self.back_button.render(window)

        window.blit(self.p_img, self.p_rect)
