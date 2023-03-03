import pygame

class Button:
    def __init__(self, text: str, font_size: int, x: float, y: float, surface: pygame.Surface) -> None:
        self.text = text
        #self.font_size = font_size
        self.x = x
        self.y = y
        self.surface = surface
        self.text_color = (0, 0, 0)
        self.box_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Courier", font_size, True)
        self.button_text = self.font.render(self.text, True, self.text_color)
        self.width = self.button_text.get_width()
        self.height = self.button_text.get_height()
        self.button_box = pygame.Rect(self.x - self.width / 2 * 1.4, self.y - self.height / 2 * 1.4, self.width * 1.4, self.height * 1.4)

    def draw_button(self):
        self.button_text = self.font.render(self.text, True, self.text_color)
        pygame.draw.rect(self.surface, self.box_color, self.button_box, 0, 2)
        self.surface.blit(self.button_text, (self.x - self.width / 2, self.y - self.height / 2))

    def hover_on_button(self):
        self.text_color = (255, 255, 255)
        self.box_color = (0, 0, 0)

    def hover_off_button(self):
        self.text_color = (0, 0, 0)
        self.box_color = (255, 255, 255)

    def is_pressed(self):
        if pygame.Rect.collidepoint(self.button_box, pygame.mouse.get_pos()):
            self.hover_on_button()
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.hover_off_button()
            return False
        
        
class Square:
    def __init__(self, x: float, y: float, width: float, height: float, surface: pygame.Surface) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.surface = surface
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.heigth)

    def draw_square(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.rectangle, 0)