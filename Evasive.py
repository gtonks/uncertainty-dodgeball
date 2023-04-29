import random
from Player import Player
from Action import Action

class Evasive(Player):
    """
    Throws the ball 35% of the time, dodges 65% of the time.
    """
    def choose_action(self, **kwargs) -> Action:
        if random.random() < 0.25:
            if self.has_ball:
                return Action.THROW
            return Action.PICK_UP
        else:
            return Action.DODGE