import pygame

class ProgressBar:
    def __init__(self, shield: str, bar: str, position: tuple[int, int]) -> None:
        self.shield_surf = pygame.image.load(shield).convert_alpha()
        self.original_bar_surf = pygame.image.load(bar).convert_alpha()
        self.bar_surf = self.original_bar_surf.copy()

        self.shield_surf = pygame.transform.scale_by(self.shield_surf, 0.5)
        self.original_bar_surf = pygame.transform.scale_by(self.original_bar_surf, 0.5)
        self.bar_surf = pygame.transform.scale_by(self.bar_surf, 0.5)

        self.shield_rect = self.shield_surf.get_rect(center=position)
        self.bar_rect = self.bar_surf.get_rect(center=position)

        self.value = 10
        self.angle = 0

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            self.angle += self.value

            if self.angle >= 180:
                self.angle = 180

            center = self.bar_rect.center 

            self.bar_surf = pygame.transform.rotate(self.original_bar_surf, self.angle)
            self.bar_rect = self.bar_surf.get_rect(center=center)

    def render(self, window: pygame.Surface):
        window.blit(self.bar_surf, self.bar_rect)
        window.blit(self.shield_surf, self.shield_rect)

