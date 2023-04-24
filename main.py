import random

from Location import Location
from Team import Team, get_players
from Half import Half
from Thrower import Thrower
from Clever import Clever
from Action import Action
from Agent import Agent
from Environment import Environment
import copy


def run_game(t1, t2):
    locations = [Location(f'l{i}') for i in range(len(t1.players))]
    team1 = copy.deepcopy(t1)
    team2 = copy.deepcopy(t2)

    team1_remaining = len(team1.players)
    team2_remaining = len(team2.players)

    while team1_remaining > 0 and team2_remaining > 0:
        for player in team1.players:
            location = random.choice(locations)
            location.team1_players.append(player)
        for player in team2.players:
            location = random.choice(locations)
            location.team2_players.append(player)

        team1_ball_pct = team1.ball_pct()
        team2_ball_pct = team2.ball_pct()

        eliminated = set()
        for location in locations:
            actions_chosen = dict()
            for action in Action:
                actions_chosen[action] = list()

            for player in location.team1_players:
                action = player.choose_action(opponent_ball_pct=team2_ball_pct)
                # print(f"Player {player.id} chose {action.name} at {location.id}.")
                actions_chosen[action].append(player)
            for player in location.team2_players:
                action = player.choose_action(opponent_ball_pct=team1_ball_pct)
                # print(f"Player {player.id} chose {action.name} at {location.id}.")
                actions_chosen[action].append(player)

            if len(actions_chosen[Action.PICK_UP]):
                random.choice(actions_chosen[Action.PICK_UP]).has_ball = True

            has_both_teams = len(location.team1_players) > 0 and len(location.team2_players) > 0
            for player in actions_chosen[Action.THROW]:
                if has_both_teams and player.has_ball:
                    if player.team == team1.id:
                        target = random.choice(location.team2_players)
                    else:
                        target = random.choice(location.team1_players)
                    if target not in actions_chosen[Action.DODGE]:
                        # For now, shots have 100% accuracy as long as the target does not dodge
                        eliminated.add(target)
                    else:
                        # 25% accuracy if the target does dodge
                        if random.random() > .75:
                            eliminated.add(target)
                player.has_ball = False

            location.team1_players.clear()
            location.team2_players.clear()

        for player in eliminated:
            if player.team == team1.id:
                team1.players.remove(player)
            else:
                team2.players.remove(player)

        team1_remaining = len(team1.players)
        team2_remaining = len(team2.players)
        # print(f"Players remaining: {team1_remaining} {team2_remaining}")

    if team1_remaining == 0 and team2_remaining == 0:
        print("Both teams have eliminated each other!")
        return None
    elif team2_remaining == 0:
        print(f"Winner: Team 1")
        return 1
    elif team1_remaining == 0:
        print(f"Winner: Team 2")
        return 2




n_games = 300
t1_wins = 0
t2_wins = 0
nPlayers = 3

t1 = Team(1, [])
t2 = Team(2, [])
agent = Agent(nPlayers, .2)
players = get_players()
for _ in range(n_games):
    env = Environment(players)
    playerIndex = agent.get_action()
    t1.add_player(players[playerIndex])
    t2.add_player()
    winner = run_game(t1, t2)
    reward = env.step(winner)
    agent.update_Q(playerIndex, reward)
    if winner == 1:
        t1_wins += 1
    elif winner == 2:
        t2_wins += 1

print(f"{t1_wins=}, {t2_wins=}")
half = 0
throw = 0
clever = 0
for player in t1.players:
    if isinstance(player, Half):
        half += 1
    elif isinstance(player, Thrower):
        throw += 1
    elif isinstance(player, Clever):
        clever += 1
print(f"Team 1:\nHalf: {half}\nThrower: {throw}\nClever: {clever}\n\n")
half = 0
throw = 0
clever = 0
for player in t2.players:
    if isinstance(player, Half):
        half += 1
    elif isinstance(player, Thrower):
        throw += 1
    elif isinstance(player, Clever):
        clever += 1
print(f"Team 2:\nHalf: {half}\nThrower: {throw}\nClever: {clever}\n\n")