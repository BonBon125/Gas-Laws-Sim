import pygame
import random


class Particle:
    def __init__(self, screen_height, screen_width) -> None:
        self.max_horizontal_position = screen_height
        self.max_vertical_position = screen_width
        self.colour = "red"
        self.size = 20
        self.position = self.get_random_position()
        self.velocity = self.get_initial_velocity()

    def get_random_position(self):
        return {"horizontal":random.randint(0 + self.size, self.max_horizontal_position - self.size), "vertical":random.randint(0 + self.size, self.max_vertical_position - self.size)}
    
    def get_initial_velocity(self):
        # first select a random number between 0 and 1
        vector_i = random.uniform(-1, 1)
        vector_j = random.uniform(-1, 1)
        return { "vector_i":vector_i, "vector_j":vector_j }

    def update_position(self, distance_to_move):
        # work out the distance to move horizontally and vertically using pythagoras
        # scale the distance
        self.wall_collision_event()
        hypotenuse = (self.velocity["vector_i"] ** 2 + self.velocity["vector_j"] ** 2) ** 0.5
        scale = distance_to_move / hypotenuse

        self.position["horizontal"] += scale * self.velocity["vector_i"]
        self.position["vertical"] += scale * self.velocity["vector_j"]
    
    def wall_collision_event(self):
        # check if the particle is touching either the left or right wall
        if self.position["horizontal"] - self.size <= 0 or self.position["horizontal"] + self.size >= self.max_horizontal_position:
            self.velocity["vector_i"] = 0 - self.velocity["vector_i"]
        if self.position["vertical"] - self.size <= 0 or self.position["vertical"] + self.size >= self.max_vertical_position:
            self.velocity["vector_j"] = 0 - self.velocity["vector_j"]


def update_particle_positions(particles):
    for i in range(len(particles)):
        particles[i].update_position(10)


def main():
    # pygame setup
    pygame.init()
    screen_height = 1280
    screen_width = 720
    number_of_particles = 100
    screen = pygame.display.set_mode((screen_height, screen_width))
    clock = pygame.time.Clock()
    running = True

    particles = []

    for i in range(number_of_particles):
        particles.append(Particle(screen_height, screen_width))
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE

        # Each particle will be in an array of particle objects


        for i in particles:
            particle_position = (i.position["horizontal"], i.position["vertical"])
            pygame.draw.circle(screen, i.colour, particle_position, i.size)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # Returns the amount of time that has passed since the previous call of this function
        # meaning the time taken for each frame
        update_particle_positions(particles)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
