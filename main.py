import pygame
import random


class Particle:
    def __init__(self, screen_height, screen_width) -> None:
        self.speed = 10
        self.max_horizontal_position = screen_height
        self.max_vertical_position = screen_width
        self.colour = "red"
        self.size = 10
        self.position = self.get_random_position()
        self.velocity = self.get_initial_velocity()

    def get_random_position(self):
        return {
            "horizontal": random.randint(
                0 + self.size, self.max_horizontal_position - self.size
            ),
            "vertical": random.randint(
                0 + self.size, self.max_vertical_position - self.size
            ),
        }

    def get_initial_velocity(self):
        # first select a random number between 0 and 1
        vector_i = random.uniform(-1, 1)
        vector_j = random.uniform(-1, 1)
        return {"vector_i": vector_i, "vector_j": vector_j}


    def update_position(self):
        hypotenuse = (
            self.velocity["vector_i"] ** 2 + self.velocity["vector_j"] ** 2
        ) ** 0.5
        scale = self.speed / hypotenuse

        self.position["horizontal"] += scale * self.velocity["vector_i"]
        self.position["vertical"] += scale * self.velocity["vector_j"]

    def wall_collision_event(self):
        # check if the particle is touching either the left or right wall
        if (
            self.position["horizontal"] - self.size <= 0
            or self.position["horizontal"] + self.size >= self.max_horizontal_position
        ):
            self.velocity["vector_i"] = 0 - self.velocity["vector_i"]
        if (
            self.position["vertical"] - self.size <= 0
            or self.position["vertical"] + self.size >= self.max_vertical_position
        ):
            self.velocity["vector_j"] = 0 - self.velocity["vector_j"]


class ParticleSystem:
    def __init__(self, num_particles, screen_height, screen_width) -> None:
        self.num_particles = num_particles
        self.particles = [Particle(screen_height, screen_width) for i in range(num_particles)]


    def update_particles(self):
        collided_particles = []
        for i in range(self.num_particles):
            for j in range(i + 1, self.num_particles):
                if self.particles_are_touching(i, j):
                    collided_particles.append(i)
                    collided_particles.append(j)
                    self.set_particle_colour(i, "blue")
                    self.set_particle_colour(j, "blue")
                elif not i in collided_particles and not j in collided_particles:
                    self.set_particle_colour(i, "red")
                    self.set_particle_colour(j, "red")



        for i in range(len(self.particles)):
            self.particles[i].wall_collision_event()
        for i in range(len(self.particles)):
            self.particles[i].update_position()

    def particles_are_touching(self, i, j):
        particle1 = self.particles[i]
        particle2 = self.particles[j]

        horizontal_distance = particle1.position["horizontal"] - particle2.position["horizontal"]
        vert_distance = particle1.position["vertical"] - particle2.position["vertical"]

        distance = (horizontal_distance ** 2 + vert_distance ** 2) ** 0.5

        if distance <= particle1.size + particle2.size:
            return True
        return False
    
    def set_particle_colour(self, index, colour):
        self.particles[index].colour = colour

def main():
    # pygame setup
    pygame.init()
    screen_height = 1280
    screen_width = 720
    number_of_particles = 100
    screen = pygame.display.set_mode((screen_height, screen_width))
    clock = pygame.time.Clock()
    running = True

    particle_system = ParticleSystem(number_of_particles, screen_height, screen_width)

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

        for i in particle_system.particles:
            particle_position = (i.position["horizontal"], i.position["vertical"])
            pygame.draw.circle(screen, i.colour, particle_position, i.size)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # Returns the amount of time that has passed since the previous call of this function
        # meaning the time taken for each frame
        particle_system.update_particles()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
