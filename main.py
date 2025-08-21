import pygame
import random


class Particle:
    def __init__(self) -> None:
        self.colour = "red"
        self.position = self.get_random_position()
        self.size = 20

    def get_random_position(self):
        return (random.randint(0, 1280), random.randint(0, 720))


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    particles = []

    for i in range(10):
        particles.append(Particle())
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # Each particle will be in an array of particle objects


        for i in particles:
            pygame.draw.circle(screen, i.colour, i.position, i.size)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # Returns the amount of time that has passed since the previous call of this function
        # meaning the time taken for each frame
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
