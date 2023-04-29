import random
import plot
from Location import Location
from Team import Team, get_players
from Half import Half
from Thrower import Thrower
from Clever import Clever
from Action import Action
from Agent import Agent
from Environment import Environment
import copy

def run_game(t1, t2, num_locations):
    locations = [Location(f'l{i}') for i in range(num_locations)]
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
                        # thrower adds .25 to hit probability
                        if isinstance(player, Thrower) and random.random() > .25:
                            eliminated.add(target)
                        elif random.random() > .5:
                            eliminated.add(target)
                    else:
                        # dodge subtracts .25 from hit probability
                        if isinstance(player, Thrower) and random.random() > .5:
                            eliminated.add(target)
                        elif random.random() > .75:
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
        locations = [Location(f'l{i}') for i in range((team1_remaining + team2_remaining) // 2)]

        if len(team1.players) == 1 and isinstance(team1.players[0], Clever) and len(team2.players) == 1 and isinstance(team2.players[0], Clever):
            return 0

    # if team1_remaining == 0 and team2_remaining == 0:
    #     print("Both teams have eliminated each other!")
    # elif team2_remaining == 0:
    #     print(f"Winner: Team 1")
    # elif team1_remaining == 0:
    #     print(f"Winner: Team 2")
    
    return team1_remaining - team2_remaining



def simulate():
    n_games = 1000 
    eps = .5
    max_team_size = 100 
    location_count = 120
    
    t1_wins = 0
    t2_wins = 0
    t1_wins_list, t2_wins_list = [], []
    nPlayers = len(get_players())

    t1 = Team(1, max_team_size, [])
    t2 = Team(2, max_team_size, [])
    agent = Agent(nPlayers, eps)
    player_choices = get_players()
    for _ in range(n_games):
        env = Environment(player_choices)
        playerIndex = agent.get_action()
        t1.add_player(
            player_choices[playerIndex],
            [type(player_choices[player_choice_index]) for player_choice_index in agent.get_remove_preference()]
        )
        t2.add_player()
        winner = run_game(t1, t2, location_count)
        reward = env.step(winner) / len(t1.players) 
        # reward = 1 if winner > 0 else 0
        agent.update_Q(playerIndex, reward)
        if winner > 0:
            t1_wins += 1
        elif winner < 0:
            t2_wins += 1

        t1_wins_list.append(t1_wins)
        t2_wins_list.append(t2_wins)
        
        print(_)
    # print(agent.Q)
    
    return t1, t2, t1_wins_list, t2_wins_list


if __name__ == "__main__":
    t1, t2, t1_wins_list, t2_wins_list = simulate()
    plot.plotWins(t1, t2, t1_wins_list, t2_wins_list)