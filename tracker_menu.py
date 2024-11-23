import pygame


class TrackerMenu:
    def __init__(self, title_path: str) -> None:
        self.title_path = title_path

        self.title_surf = pygame.image.load(title_path)
        self.title_rect = self.title_surf.get_rect(center=(1280 / 2, 100))

    def handle_events(self, event: pygame.Event):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        self.title_surf.convert_alpha()

        screen.blit(self.title_surf, self.title_rect)
