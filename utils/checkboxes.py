import pygame


class Checkbox:
    # TODO: Dodać jej metody
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

        self.images = [
            pygame.image.load("../Assets/TaskMenu/Circles/CircleOff.png"),
            pygame.image.load("../Assets/TaskMenu/Circles/CircleOn.png"),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect(topright=self.position)

        self.checked = False
