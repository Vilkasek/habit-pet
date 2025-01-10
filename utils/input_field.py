import pygame


class InputField:
    def __init__(self, position: tuple[int, int], size: tuple[int, int]) -> None:
        self.position = position
        self.size = size

        self.surf = pygame.Surface(self.size)
        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect(center=self.position)

        self.visible = False

        self.text = ""

        self.font = pygame.font.Font(None, 64)


    def is_special_key(self, key):
        return key in [pygame.K_RETURN, pygame.K_BACKSPACE, pygame.K_LSHIFT, pygame.K_RSHIFT,
            pygame.K_CAPSLOCK, pygame.K_ESCAPE, pygame.K_LMETA, pygame.K_RMETA]

    def handle_events(self, event: pygame.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if not self.is_special_key(event.key):
                    if event.key == pygame.K_SPACE:
                        self.text += " "
                    else:
                        self.text += pygame.key.name(event.key)
                    
                    self.text = self.text.upper()

    def clear_field(self):
        self.text = ""
    
    def render(self, screen: pygame.Surface):
        if self.visible:
            text_surf = self.font.render(self.text, True, (0,0,0))
            text_rect = text_surf.get_rect(topleft=(self.rect.topleft[0] + 10, self.rect.topleft[1] + 10))
            
            screen.blit(self.surf, self.rect)
            screen.blit(text_surf, text_rect)
