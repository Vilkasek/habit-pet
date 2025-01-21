import pygame


class ProgressBar:
    def __init__(self, shield: str, bar: str, positon: tuple[int, int]) -> None:
        self.shield_surf = pygame.image.load(shield)
        self.bar_surf = pygame.image.load(bar)

        self.shield_rect = self.shield_surf.get_rect(center=positon)
        self.bar_rect = self.bar_surf.get_rect(center=positon)

    def render(self, window: pygame.Surface):
        self.shield_surf = self.shield_surf.convert_alpha()
        self.bar_surf = self.bar_surf.convert_alpha()

        window.blit(self.bar_surf, self.bar_rect)
        window.blit(self.shield_surf, self.shield_rect)
