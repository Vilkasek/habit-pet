import pygame


class Paw:
    def __init__(
        self, image_path: str, position: tuple[int, int], flipped: bool, delay: int = 0
    ):
        self.flipped = flipped

        if not self.flipped:
            self.image: pygame.Surface = pygame.image.load(image_path)
        else:
            self.image: pygame.Surface = pygame.image.load(image_path)
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.alpha: int = 0
        self.image.set_alpha(self.alpha)

        self.delay: int = delay
        self.time_since_last_update: int = 0
        self.fading_in: bool = True

    def update(self, dt: int):
        self.time_since_last_update += dt

        if self.time_since_last_update >= self.delay:
            if self.fading_in:
                if self.alpha < 255:
                    self.alpha += 2
                else:
                    self.fading_in = False
            else:
                if self.alpha > 0:
                    self.alpha -= 2
                else:
                    self.fading_in = True

            self.image.set_alpha(self.alpha)
            self.time_since_last_update = 0

    def draw(self, window: pygame.Surface):
        self.image = self.image.convert_alpha()
        window.blit(self.image, self.rect)
