import pygame


class Hint:
    def __init__(self, image_path: str, position: tuple[int, int]):
        self.image: pygame.Surface = pygame.image.load(image_path)
        self.rect: pygame.Rect = self.image.get_rect(center=position)

        self.visible: bool = False
        self.alpha: int = 0

        self.image.set_alpha(self.alpha)

    def update(self, button_hovered: bool):
        if button_hovered:
            if self.alpha < 255:
                self.alpha += 30
        else:
            if self.alpha > 0:
                self.alpha -= 30

        self.image.set_alpha(self.alpha)

        self.visible = self.alpha > 0

    def draw(self, window: pygame.Surface):
        self.image = self.image.convert_alpha()

        if self.visible:
            window.blit(self.image, self.rect)
