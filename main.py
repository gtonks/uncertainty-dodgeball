import random

from Location import Location
from Thrower import Thrower
from Half import Half
from Clever import Clever
from Action import Action


def ball_pct(team: list) -> float:
    """
    Returns the percent of the team that has a ball.
    """
    total = 0
    with_ball = 0
    for player in team:
        if player.has_ball == True:
            with_ball += 1
        total += 1
    return with_ball / total


locations = [Location(f'l{i}') for i in range(2)]
team1_id = 1
team1 = [Thrower(f't{i}', team1_id) for i in range(1)]
team2_id = 2
# team2 = [Half(f'h{i}', team2_id) for i in range(2)]
team2 = [Clever(f'c{i}', team2_id) for i in range(1)]

while len(team1) > 0 and len(team2) > 0:
    print(f"Players remaining: {len(team1)} {len(team2)}")

    for player in team1:
        location = random.choice(locations)
        location.team1_players.append(player)
    for player in team2:
        location = random.choice(locations)
        location.team2_players.append(player)

    team1_ball_pct = ball_pct(team1)
    team2_ball_pct = ball_pct(team2)

    eliminated = set()
    for location in locations:
        actions_chosen = dict()
        for action in Action:
            actions_chosen[action] = list()

        for player in location.team1_players:
            action = player.choose_action(opponent_ball_pct=team2_ball_pct)
            print(f"Player {player.id} chose {action.name} at {location.id}.")
            actions_chosen[action].append(player)
        for player in location.team2_players:
            action = player.choose_action(opponent_ball_pct=team1_ball_pct)
            print(f"Player {player.id} chose {action.name} at {location.id}.")
            actions_chosen[action].append(player)

        if len(actions_chosen[Action.PICK_UP]) == 1:
            actions_chosen[Action.PICK_UP][0].has_ball = True

        has_both_teams = len(location.team1_players) > 0 and len(location.team2_players) > 0
        for player in actions_chosen[Action.THROW]:
            if has_both_teams and player.has_ball:
                if player.team == team1_id:
                    target = random.choice(location.team2_players)
                else:
                    target = random.choice(location.team1_players)
                if target not in actions_chosen[Action.DODGE]:
                    # For now, shots have 100% accuracy as long as the target does not dodge
                    eliminated.add(target)
            player.has_ball = False

        location.team1_players.clear()
        location.team2_players.clear()

    for player in eliminated:
        if player.team == team1_id:
            team1.remove(player)
        else:
            team2.remove(player)

print(f"Winner: Team {1 if len(team2) == 0 else 2}")
