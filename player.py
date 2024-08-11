import pygame

class Player:
    MAX_SPEED = 300
    RADIUS = 40

    def __init__(self, pos):
        self._pos = pos.copy()
        self._prev_pos = pos.copy()

    def pos(self):
        return self._pos

    def step(self, world, dt):
        self._prev_pos.update(self._pos)
        self._pos += world.controller_direction * Player.MAX_SPEED * dt
    
    def handle_collision(self, world, mob):
        self._pos.update(self._prev_pos)

    