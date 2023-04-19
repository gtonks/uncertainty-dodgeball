import random

from Player import Player
from Action import Action


class Half(Player):
    """
    Dodges half of the time.
    """
    def choose_action(self, **kwargs) -> Action:
        if random.random() < 0.5:
            return Action.DODGE
        if self.has_ball:
            return Action.THROW
        return Action.PICK_UP
