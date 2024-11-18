import sys

import pygame


class HabitPet:
    def __init__(self, size: tuple[int, int], title="Habit Pet"):
        pygame.init()

        self.size = size
        self.width, self.height = size

        self.title = title
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.clock.tick(60)

    def render(self):
        self.screen.fill((5, 31, 57))
        pygame.display.flip()

    def run(self):
        while True:
            self.update()
            self.render()


if __name__ == "__main__":
    app = HabitPet((1280, 720))
    app.run()
