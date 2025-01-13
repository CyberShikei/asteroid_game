#!venv/bin/python3
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_TITLE

from player import Player

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

    # clock to control the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # create a player object
    player = Player(SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2
                    )

    # Create updateable and drawable groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add the player to the groups
    updateable.add(player)
    drawable.add(player)

    # Start the game loop
    running = True
    while running:
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # On key plress q or esc, quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

        # fill the screen with black
        screen.fill((0, 0, 0))

        # update
        for updateable_sprite in updateable:
            updateable_sprite.update(dt)

        # draw
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        # update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
