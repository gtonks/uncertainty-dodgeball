from Player import Player
from Action import Action


class Thrower(Player):
    def choose_action(self) -> Action:
        if self.has_ball:
            return Action.THROW
        return Action.PICK_UP
