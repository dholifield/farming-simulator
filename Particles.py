import Constants as c

class Particle:
    def __init__(self, x, y, color, size, lifespan):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.lifespan = lifespan
        self.age = 0
        self.velocity = [c.uniform(-1, 1), c.uniform(0, 1)]
        self.is_dead = False

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.age += 1
        if self.age > self.lifespan:
            self.is_dead = True

    def draw(self, screen):
        c.pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


class ParticleSystem:
    def __init__(self, color):
        self.particles = []
        self.color = color

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if not p.is_dead]
    
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

    def spawn_particle(self, x, y):
        new_particle = Particle(x + c.uniform(-5, 5), y + c.uniform(-5, 5), self.color, 2, 60)
        self.particles.append(new_particle)