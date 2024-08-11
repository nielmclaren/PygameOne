import pygame
import random
from mob import Mob

class World:
    def __init__(self, size):
        (w, h) = size
        self.player_pos = pygame.Vector2(w / 2, h / 2)
        self.player_speed = 300
        self.mob = Mob(pygame.Vector2(random.random() * w, random.random() * h))
        self.controller_direction = pygame.Vector2()

    def set_controller(self, direction):
        self.controller_direction = direction

    def estimate_player_pos(self, delay):
        return self.player_pos + self.controller_direction * self.player_speed * delay / 1000
    
    def step(self, dt):
        self.player_pos += self.controller_direction * self.player_speed * dt

        self.mob.step(self, dt)