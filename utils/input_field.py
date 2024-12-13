import pygame


class InputField:
    def __init__(self, position: tuple[int, int], size: tuple[int, int]) -> None:
        self.position = position
        self.size = size

        self.surf = pygame.Surface(self.size)
        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect(center=self.position)

        self.visible = False

    def render(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
