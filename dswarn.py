import random
import sys

import pygame

from text_message import TextMessage

DISPLAY_TIME_MS = 2000
COLOR_CHANGE_TIME_MS = 100
FPS = 60
MESSAGE_SPEED = -1.0
PADDING_SIZE = 4


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def create_text_message(message, font, size, color):
    text_message = TextMessage()
    text_message.font = font
    text_message.size = size
    text_message.color = color
    text_message.message = message
    text_message.render_text()
    return text_message


def main():
    padding = ' ' * PADDING_SIZE
    message = padding + sys.argv[1] + padding
    start_time = pygame.time.get_ticks()
    pygame.init()
    text_message = create_text_message(message, 'Sans', 128, (0, 0, 0))
    main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32, 0)

    clock = pygame.time.Clock()
    last_color_update = start_time
    color = (0, 0, 0)

    while pygame.time.get_ticks() - start_time < DISPLAY_TIME_MS:
        delta = clock.tick(FPS)
        text_message.update_cursor(delta * MESSAGE_SPEED)
        if pygame.time.get_ticks() - last_color_update > COLOR_CHANGE_TIME_MS:
            color = random_color()
            last_color_update = pygame.time.get_ticks()
        main_surface.fill(color)
        text_message.blit_to_screen(main_surface, main_surface.get_rect())
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
