import pygame
from mob_state import MobState

class Mob:
    MAX_SPEED = 400
    RADIUS = 40

    def __init__(self, pos):
        self._pos = pos.copy()
        self._prev_pos = pos.copy()
        self._target_pos = None
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()

    def pos(self):
        return self._pos

    def step(self, world, dt):
        match self.state:
            case MobState.RESTING:
                return self._step_resting(world, dt)
            case MobState.MOVING:
                return self._step_moving(world, dt) 

    def handle_collision(self, world, player):
        self._pos.update(self._prev_pos)
        self._change_state_resting(world)
    
    def _step_resting(self, world, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 500):
            self._change_state_moving(world)
    
    def _step_moving(self, world, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 250):
            self._change_state_resting(world)

        if (self._target_pos):
            direction = (self._target_pos - self._pos).normalize()
            self._prev_pos.update(self._pos)
            self._pos += direction * Mob.MAX_SPEED * dt
    
    def _change_state_moving(self, world):
        self.state = MobState.MOVING
        self.state_change_time = pygame.time.get_ticks()

        self._target_pos = world.estimate_player_pos(500).copy()

    def _change_state_resting(self, world):
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()
        
