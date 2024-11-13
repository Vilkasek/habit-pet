import os

import pygame


class Paw:
    def __init__(self, folder_path: str, pos: tuple[int, int], framerate: int) -> None:
        self.position = pos

        self.folder_path = folder_path
        self.framerate = framerate

        self.frame_index = 0
        self.frames = []

        self.last_update = pygame.time.get_ticks()

        for filename in sorted(os.listdir(self.folder_path)):
            if filename.endswith(".png"):
                frame = pygame.image.load(os.path.join(folder_path, filename))
                self.frames.append(frame)

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > 1000 // self.framerate:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def draw(self, window: pygame.Surface):
        current_frame = self.frames[self.frame_index]
        current_frame = pygame.transform.scale(current_frame, (400, 400))
        current_frame = current_frame.convert_alpha()

        frame_rect = current_frame.get_rect(center=self.position)

        window.blit(current_frame, frame_rect)
