from Player import Player
from Action import Action


class Clever(Player):
    """
    Devensive when the other team has a lot of balls and vice versa.
    """
    def choose_action(self, opponent_ball_pct, **kwargs) -> Action:
        if opponent_ball_pct > 0.5:
            return Action.DODGE
        if self.has_ball:
            return Action.THROW
        return Action.PICK_UP
