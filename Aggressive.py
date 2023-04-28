import random
from Player import Player
from Action import Action

class Aggressive(Player):
    """
    Throws the ball 75% of the time, dodges 25% of the time.
    """
    def choose_action(self, **kwargs) -> Action:
        if random.random() < 0.75:
            if self.has_ball:
                return Action.THROW
            return Action.PICK_UP
        else:
            return Action.DODGE