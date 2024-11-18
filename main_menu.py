import pygame


class MainMenu:
    def __init__(self, title_path: str) -> None:
        self.title_path = title_path

        self.title_surf = pygame.image.load(title_path)
        self.title_rect = self.title_surf.get_rect(center=(1280 / 2, 100))

        self.test_buttons_paths = [
            "./Assets/MainMenu/Buttons/Start.png",
            "./Assets/MainMenu/Buttons/Options.png",
            "./Assets/MainMenu/Buttons/Exit.png",
        ]

        self.test_buttons_surfs = []

        for path in self.test_buttons_paths:
            self.test_buttons_surfs.append(pygame.image.load(path))

        self.test_buttons_rects = [
            self.test_buttons_surfs[0].get_rect(center=(1280 / 2, 300)),
            self.test_buttons_surfs[1].get_rect(center=(1280 / 2, 380)),
            self.test_buttons_surfs[2].get_rect(center=(1280 / 2, 460)),
        ]

    def handle_events(self, event: pygame.Event):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        self.title_surf = self.title_surf.convert_alpha()

        for surf in self.test_buttons_surfs:
            surf = surf.convert_alpha()

        screen.blit(self.title_surf, self.title_rect)

        for i in range(3):
            screen.blit(self.test_buttons_surfs[i], self.test_buttons_rects[i])
