import pygame
from mob_state import MobState

class Mob:
    def __init__(self, pos):
        self.pos = pos
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()

    def step(self, world, dt):
        match self.state:
            case MobState.RESTING:
                return self.__step_resting(world, dt)
            case MobState.MOVING:
                return self.__step_moving(world, dt) 
    
    def __step_resting(self, world, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 500):
            self.__change_state_moving(world, dt)
    
    def __step_moving(self, world, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 250):
            self.__change_state_resting(world, dt)

        direction = (self.target_pos - self.pos).normalize()
        self.pos += direction * 400 * dt
    
    def __change_state_moving(self, world, dt):
        self.state = MobState.MOVING
        self.state_change_time = pygame.time.get_ticks()

        self.target_pos = world.estimate_player_pos(500).copy()

    def __change_state_resting(self, world, dt):
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()
        
