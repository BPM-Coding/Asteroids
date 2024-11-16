import pygame

from circleshape import CircleShape

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN

from shot import Shot

class Player(CircleShape): 
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shottimer = 0
        # Logic to add this player instance to all associated groups
        for group in self.containers:
            group.add(self)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shottimer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if self.shottimer > 0:
            return
        self.shottimer = PLAYER_SHOT_COOLDOWN
        # A new shot instance has to be created to shoot, at the player's position
        new_shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1)
        # The shot also has to face the same way as the player
        velocity = velocity.rotate(self.rotation)
        velocity *= PLAYER_SHOOT_SPEED
        # The shot's velocity calculations all needs to be saved here
        new_shot.velocity = velocity
        

        