import pygame


class TextMessage:
    def __init__(self):
        self.message = None
        self.font = None
        self.size = None
        self.color = None
        self.surface = None
        self.cursor_x = None

    def render_text(self):
        self.surface = pygame.font.SysFont(self.font, self.size).render(self.message, False, self.color)
        self.cursor_x = 0.0

    def blit_to_screen(self, screen, rect):
        blit_y = self._get_message_y(rect)
        blit_x = int(self.cursor_x)
        draw_x = 0
        screen.blit(self.surface, (blit_x, blit_y))

    def update_cursor(self, delta_x):
        self.cursor_x += delta_x
        while self.cursor_x > self.surface.get_rect().w:
            self.cursor_x -= self.surface.get_rect().w
        while self.cursor_x < 0:
            self.cursor_x += self.surface.get_rect().w

    def _get_message_y(self, rect):
        return (rect.h // 2) - (self.surface.get_rect().h // 2)
