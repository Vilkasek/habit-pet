import pygame

from utils.button import Button
from utils.states import State
from utils.progress_bar import ProgressBar

class Petroom:
    def __init__(self, path: str) -> None:
        self.p_img: pygame.Surface = pygame.image.load(path)
        self.p_rect = self.p_img.get_rect(center=(640,360))

        self.state = State()

        self.back_button = Button("./Assets/TaskMenu/Controls/Back.png", (60, 660))

        self.ui = [
            ProgressBar("./Assets/Pet/UI/health_shield.png", "./Assets/Pet/UI/health_bar.png", (170, 200)),
            ProgressBar("./Assets/Pet/UI/energy_shield.png", "./Assets/Pet/UI/energy_bar.png", (170, 400)),
            ProgressBar("./Assets/Pet/UI/fun_shield.png", "./Assets/Pet/UI/fun_bar.png", (170, 600)),
        ]

    def handle_events(self, event: pygame.Event):
        mouse_pos = pygame.mouse.get_pos()

        if self.back_button.is_clicked(event, mouse_pos):
            self.state.change_state("tracker")

    def update(self) -> None:
        pass

    def render(self, window: pygame.Surface) -> None:
        self.p_img = self.p_img.convert_alpha()
        
        self.back_button.render(window)

        for element in self.ui:
            element.render(window)

        window.blit(self.p_img, self.p_rect)
