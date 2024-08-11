
class Mob:
    def __init__(self, pos):
        self.pos = pos

    def step(self, player_pos, dt):
       direction = (player_pos - self.pos).normalize()
       self.pos += direction * 200 * dt
       