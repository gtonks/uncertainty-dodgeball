import random

from Location import Location
from Thrower import Thrower
from Half import Half
from Action import Action


locations = [Location()]
team1_id = 1
team1 = [Thrower(1, team1_id)]
team2_id = 2
team2 = [Half(2, team2_id)]

while len(team1) > 0 and len(team2) > 0:
    print(f"Players remaining: {len(team1)} {len(team2)}")

    for player in team1:
        location = random.choice(locations)
        location.team1_players.append(player)
    for player in team2:
        location = random.choice(locations)
        location.team2_players.append(player)

    eliminated = list()
    for location in locations:
        actions_chosen = dict()
        for action in Action:
            actions_chosen[action] = list()

        for player in location.team1_players + location.team2_players:
            action = player.choose_action()
            print(f"Player {player.id} chose {action.name}.")
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
                    eliminated.append(target)
            player.has_ball = False

        location.team1_players.clear()
        location.team2_players.clear()

    for player in eliminated:
        if player.team == team1_id:
            team1.remove(player)
        else:
            team2.remove(player)

print(f"Winner: Team {1 if len(team2) == 0 else 2}")
