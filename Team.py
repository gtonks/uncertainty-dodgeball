class Team:
    def __init__(self, id, players: list) -> None:
        self.id = id
        self.players = players

    def ball_pct(self) -> float:
        """
        Returns the percent of the team that has a ball.
        """
        total = 0
        with_ball = 0
        for player in self.players:
            if player.has_ball == True:
                with_ball += 1
            total += 1
        return with_ball / total
