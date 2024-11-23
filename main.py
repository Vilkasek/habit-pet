import sys

import pygame

from main_menu import MainMenu
from tracker_menu import TrackerMenu
from utils.states import State


class HabitPet:
    def __init__(self, size: tuple[int, int], title="Habit Pet"):
        pygame.init()

        self.size = size
        self.width, self.height = size

        self.title = title
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.state = State()

        self.main_menu = MainMenu("./Assets/MainMenu/Habit pet.png")
        self.tracker_menu = TrackerMenu("./Assets/TaskMenu/Your tasks.png")

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            match self.state.state:
                case "main-menu":
                    self.main_menu.handle_events(event)
                case "tracker":
                    self.tracker_menu.handle_events(event)

    def update(self):
        match self.state.state:
            case "main-menu":
                self.main_menu.update()
            case "tracker":
                self.tracker_menu.update()

        self.clock.tick(60)

    def render(self):
        self.screen.fill((5, 31, 57))

        match self.state.state:
            case "main-menu":
                self.main_menu.render(self.screen)
            case "tracker":
                self.tracker_menu.render(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_event()
            self.update()
            self.render()


if __name__ == "__main__":
    app = HabitPet((1280, 720))
    app.run()
