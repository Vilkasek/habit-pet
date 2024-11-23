import pygame

from utils.button import Button
from utils.states import State


class MainMenu:
    def __init__(self, title_path: str) -> None:
        self.title_path = title_path

        self.title_surf = pygame.image.load(title_path)
        self.title_rect = self.title_surf.get_rect(center=(1280 / 2, 100))

        self.mouse_pos: tuple[int, int] = (0, 0)

        self.buttons = [
            Button("./Assets/MainMenu/Buttons/Start.png", (640, 300)),
            Button("./Assets/MainMenu/Buttons/Options.png", (640, 380)),
            Button("./Assets/MainMenu/Buttons/Exit.png", (640, 460)),
        ]

        self.paw_anim_frames_right = [
            pygame.image.load("./Assets/MainMenu/Paw_Animation/1.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/2.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/3.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/4.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/5.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/6.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/7.png"),
            pygame.image.load("./Assets/MainMenu/Paw_Animation/8.png"),
        ]
        self.paw_index = 0
        self.paw_frame_right = self.paw_anim_frames_right[self.paw_index]
        self.paw_rect_right = self.paw_frame_right.get_rect(topleft=(0, 200))

        self.paw_anim_frames_left = []
        for paw in self.paw_anim_frames_right:
            self.paw_anim_frames_left.append(paw)

        self.state = State()

    def handle_events(self, event: pygame.Event):
        if self.buttons[0].is_clicked(event, self.mouse_pos):
            self.state.change_state("tracker")
        if self.buttons[1].is_clicked(event, self.mouse_pos):
            pass
        if self.buttons[2].is_clicked(event, self.mouse_pos):
            pygame.quit()

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.paw_index += 0.01

        if self.paw_index >= 8:
            self.paw_index = 0

        self.paw_frame_right = self.paw_anim_frames_right[int(self.paw_index)]

    def render(self, screen: pygame.Surface):
        self.title_surf = self.title_surf.convert_alpha()

        self.paw_frame_right = self.paw_frame_right.convert_alpha()
        self.paw_frame_right = pygame.transform.scale(self.paw_frame_right, (400, 400))

        paw_left = pygame.transform.flip(self.paw_frame_right, True, False)
        paw_left_rect = paw_left.get_rect(topright=(1280, 200))

        for button in self.buttons:
            button.render(screen)

        screen.blit(self.title_surf, self.title_rect)

        screen.blit(paw_left, paw_left_rect)
        screen.blit(self.paw_frame_right, self.paw_rect_right)
