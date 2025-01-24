import pygame
import json

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
            Button("./Assets/Pet/Door/drzwi_cale.png", (1100, 600))
        ]

        self.tasks = []
        self.position_y = 250

        self.state = State()
        self.inputfield = InputField((640, 580), (600, 60))

        self.full = False
        self.tasks_amount = 0

        self.load_tasks_from_file()
 
    def save_tasks_to_file(self, filename="./miscs/tasks.json"):
        tasks_data = []
        for task in self.tasks:
            task_name = task.text
            task_pos = task.position[1]
            checkbox_states = [checkbox.checked for checkbox in task.checkboxes]
            tasks_data.append({"task": task_name, "checkboxes": checkbox_states, "position": task_pos})
        with open(filename, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def load_tasks_from_file(self, filename="./miscs/tasks.json"):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
            for task in tasks_data:
                self.tasks.append(Task(task.task, (400, task.position)))
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty task list.")


    def handle_events(self, event: pygame.Event):
        if self.buttons[0].is_clicked(event, self.mouse_pos):
            self.save_tasks_to_file()
            self.state.change_state("main-menu")
        if self.buttons[1].is_clicked(event, self.mouse_pos):
            self.add_task()
        if self.buttons[2].is_clicked(event, self.mouse_pos):
            self.state.change_state("pet-room")

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
