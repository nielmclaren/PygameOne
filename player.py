import pygame

class Player:
    MAX_SPEED = 300

    def __init__(self, pos):
        self.pos = pos

    def step(self, world, dt):
        self.pos += world.controller_direction * self.MAX_SPEED * dt

    