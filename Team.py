from Half import Half
from Clever import Clever
from Thrower import Thrower
from Aggressive import Aggressive
from Evasive import Evasive
import random
import copy

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
    
    def add_player(self, player=None):
        if self.id == 1:
            newPlayer = copy.deepcopy(player)
            newPlayer.id = f'p{len(self.players) + 1}'
            newPlayer.team = 1
            self.players.append(newPlayer)
            # print(f"Team 1 added player {type(player)}")
        else:
            players = get_players()
            player = random.choice(players)
            newPlayer = copy.deepcopy(player)
            newPlayer.id = f'p{len(self.players) + 1}'
            newPlayer.team = 2
            self.players.append(newPlayer)
            # print(f"Team 2 added player {type(player)}")

def get_players():    
    players = [
        # Half(None,None),
        # Half(None,None),
        # Half(None,None),
        # Half(None,None),
        # Half(None,None),
        Evasive(None,None),
        Aggressive(None,None),
        Half(None,None),
        Thrower(None,None),
        Clever(None,None),
    ]
    
    return players
