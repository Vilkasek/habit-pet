import pygame


class Button:
    def __init__(self, path: str, pos: tuple[int, int]) -> None:
        self.path = path
        self.pos = pos

        self.surf = pygame.image.load(self.path)
        self.rect = self.surf.get_rect(center=self.pos)

    def is_clicked(self, event: pygame.Event, mouse_pos: tuple[int, int]) -> bool:
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(mouse_pos):
            return True
        return False

    def render(self, screen: pygame.Surface):
        self.surf = self.surf.convert_alpha()

        screen.blit(self.surf, self.rect)
