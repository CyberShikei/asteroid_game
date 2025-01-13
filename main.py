#!venv/bin/python3
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_TITLE

WELCOME_MESSAGE = "Welcome to Asteroids!"
START_MESSAGE = "Starting asteroids!"


def main():
    print(START_MESSAGE)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize the pygame library
    pygame.init()

    # create a window with the specified dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set the title of the window
    pygame.display.set_caption(GAME_TITLE)

    # Start the game loop
    running = True
    while running:
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with black
        screen.fill((0, 0, 0))

        # update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
