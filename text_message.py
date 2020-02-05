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

    def blit_to_screen(self, screen, dest_rect):
        dest_y = self._get_message_y(dest_rect)
        src_x = int(self.cursor_x)
        dest_x = 0
        src_rect = pygame.Rect(src_x, 0, self.surface.get_rect().w - src_x, self.surface.get_rect().h)
        screen.blit(self.surface, (dest_x, dest_y), src_rect)
        dest_x += src_rect.w
        while dest_x < dest_rect.w:
            src_rect = self._make_source_rect(dest_x, dest_rect)
            screen.blit(self.surface, (dest_x, dest_y), src_rect)
            dest_x += src_rect.w

    def update_cursor(self, delta_x):
        self.cursor_x += delta_x
        while self.cursor_x > self.surface.get_rect().w:
            self.cursor_x -= self.surface.get_rect().w
        while self.cursor_x < 0:
            self.cursor_x += self.surface.get_rect().w

    def _get_message_y(self, rect):
        return (rect.h // 2) - (self.surface.get_rect().h // 2)

    def _make_source_rect(self, dest_x, dest_rect):
        source_rect = pygame.Rect(self.surface.get_rect().x, self.surface.get_rect().y, 0, self.surface.get_rect().h)
        dest_remaining_width = dest_rect.w - dest_x
        if dest_remaining_width < self.surface.get_rect().w:
            source_rect.w = dest_remaining_width
        else:
            source_rect.w = self.surface.get_rect().w
        print(source_rect)
        return source_rect
