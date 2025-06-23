# cd github.com/Asteroids
# source venv/bin/activate

# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Creates a clock object
    # this helps with the framerate and tracking the time in frames
    clock = pygame.time.Clock()
    # Variable being used for delta time
    dt = 0
    while True:
        # If the X to close the window is clicked, the window closes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        # Sets the framerate to 60 frames
        clock.tick(60)
        # Converts the milliseconds of frames to seconds
        dt = clock.tick(60) / 1000

        




    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
    