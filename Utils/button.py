import pygame


class Button:
    def __init__(self, image_path: str, position: tuple[int, int]):
        self.image: pygame.Surface = pygame.image.load(image_path)
        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.clicked = False

    def draw(self, window: pygame.Surface):
        self.image = self.image.convert_alpha()

        window.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos: tuple[int, int], event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(mouse_pos):
            return True

        return False
