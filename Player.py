from Action import Action


class Player:
    """
    Abstract class for players.
    """
    def __init__(self, id, team) -> None:
        self.id = id
        self.team = team
        self.has_ball = False

    def choose_action(self, **kwargs) -> Action:
        raise NotImplementedError
