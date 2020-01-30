import random
import sys

import pygame

DISPLAY_TIME_MS = 2000
COLOR_CHANGE_TIME_MS = 100
FPS = 60
MESSAGE_SPEED = -1.0


def get_message_y(main_surface, message_surface):
    return (main_surface.get_rect().h // 2) - (message_surface.get_rect().h // 2)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def main():
    message = sys.argv[1]
    start_time = pygame.time.get_ticks()
    pygame.init()
    message_surface = pygame.font.SysFont('Sans', 128).render(message, False, (0, 0, 0))
    main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32, 0)
    message_x = 0.0
    message_y = get_message_y(main_surface, message_surface)

    clock = pygame.time.Clock()
    last_color_update = start_time
    color = (0, 0, 0)

    while pygame.time.get_ticks() - start_time < DISPLAY_TIME_MS:
        delta = clock.tick(FPS)
        message_x += delta * MESSAGE_SPEED
        print(delta)
        print(message_x)
        if pygame.time.get_ticks() - last_color_update > COLOR_CHANGE_TIME_MS:
            color = random_color()
            last_color_update = pygame.time.get_ticks()
        main_surface.fill(color)
        main_surface.blit(message_surface, (int(message_x), message_y))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
