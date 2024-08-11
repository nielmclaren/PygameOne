import pygame
import random
from mob import Mob
from player import Player

class World:
    def __init__(self, size):
        (w, h) = size
        self.player = Player(pygame.Vector2(w/2, h/2))
        self.mob = Mob(pygame.Vector2(random.random() * w, random.random() * h))
        self.controller_direction = pygame.Vector2()

    def set_controller(self, direction):
        self.controller_direction = direction

    def estimate_player_pos(self, delay):
        return self.player.pos + self.controller_direction * Player.MAX_SPEED * delay / 1000
    
    def step(self, dt):
        self.player.step(self, dt)
        self.mob.step(self, dt)
    