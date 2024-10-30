import pygame


class Hint:
    def __init__(self, image_path: str, position: tuple[int, int]):
        self.image: pygame.Surface = pygame.image.load(image_path)
        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.visible: bool = False

    def update(self, button_hovered: bool):
        if button_hovered:
            self.visible = True
        else:
            self.visible = False

    def draw(self, window: pygame.Surface):
        self.image = self.image.convert_alpha()

        if self.visible:
            window.blit(self.image, self.rect)
