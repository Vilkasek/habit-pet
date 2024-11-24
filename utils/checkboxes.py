import pygame


class Checkbox:
    def __init__(self, on_path: str, off_path: str, position: tuple[int, int]) -> None:
        self.position = position

        self.images = [
            pygame.image.load(off_path),
            pygame.image.load(on_path),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect(topright=self.position)

        self.checked = False

        self.mouse_pos = (0, 0)

    def handle_events(self, event: pygame.Event):
        if (
            self.rect.collidepoint(self.mouse_pos)
            and event.type == pygame.MOUSEBUTTONUP
        ):
            self.checked = not self.checked

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        self.image_index = int(self.checked)

        self.image = self.images[self.image_index]

    def render(self, screen: pygame.Surface):
        self.image = self.image.convert_alpha()

        screen.blit(self.image, self.rect)
