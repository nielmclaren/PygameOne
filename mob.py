import pygame
from mob_state import MobState

class Mob:
    def __init__(self, pos):
        self.pos = pos
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()

    def step(self, player_pos, dt):
        match self.state:
            case MobState.RESTING:
                return self.__step_resting(player_pos, dt)
            case MobState.MOVING:
                return self.__step_moving(player_pos, dt) 
    
    def __step_resting(self, player_pos, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 500):
            self.__change_state_moving(player_pos, dt)
    
    def __step_moving(self, player_pos, dt):
        if (pygame.time.get_ticks() - self.state_change_time > 250):
            self.__change_state_resting(player_pos, dt)

        direction = (self.target_pos - self.pos).normalize()
        self.pos += direction * 400 * dt
    
    def __change_state_moving(self, player_pos, dt):
        self.state = MobState.MOVING
        self.state_change_time = pygame.time.get_ticks()

        self.target_pos = player_pos.copy()

    def __change_state_resting(self, player_pos, dt):
        self.state = MobState.RESTING
        self.state_change_time = pygame.time.get_ticks()
        
