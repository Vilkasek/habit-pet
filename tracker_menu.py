import pygame

from tasks import Task
from utils.button import Button
from utils.states import State
from utils.input_field import InputField


class TrackerMenu:
    def __init__(self, title_path: str) -> None:
        self.title_path = title_path

        self.title_surf = pygame.image.load(title_path)
        self.title_rect = self.title_surf.get_rect(center=(1280 / 2, 100))

        self.mouse_pos = (0, 0)

        self.buttons = [
            Button("./Assets/TaskMenu/Controls/Back.png", (60, 660)),
            Button("./Assets/TaskMenu/Controls/AddTaskButton.png", (640, 660)),
        ]

        self.tasks = []
        self.position_y = 250

        self.state = State()
        self.inputfield = InputField((640, 580), (600, 60))

        self.full = False
        self.tasks_amount = 0

    def handle_events(self, event: pygame.Event):
        if self.buttons[0].is_clicked(event, self.mouse_pos):
            self.state.change_state("main-menu")
        if self.buttons[1].is_clicked(event, self.mouse_pos):
            self.add_task()

        if (
            self.inputfield.visible
            and event.type == pygame.KEYUP
            and event.key == pygame.K_RETURN
        ):
            self.inputfield.visible = False
            self.tasks_amount += 1

            if self.tasks_amount <= 6:
                self.create_tasks()
        elif self.inputfield.visible and event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            self.inputfield.visible = False
            self.inputfield.clear_field()

        if self.inputfield.visible:
            self.inputfield.handle_events(event)

        for task in self.tasks:
            task.handle_events(event)

    def add_task(self):
        self.inputfield.visible = True

    def create_tasks(self):
        if not self.full:
            self.tasks.append(Task(self.inputfield.text, (400, self.position_y)))
            self.inputfield.clear_field()

            for task in self.tasks:
                task.create_checkboxes()

            self.position_y += 60

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        for task in self.tasks:
            task.update()

    def render(self, screen: pygame.Surface):
        self.title_surf.convert_alpha()

        for button in self.buttons:
            button.render(screen)

        for task in self.tasks:
            task.render(screen)

        self.inputfield.render(screen)

        screen.blit(self.title_surf, self.title_rect)
