import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Half import Half
from Thrower import Thrower
from Clever import Clever
from Aggressive import Aggressive
from Evasive import Evasive
from Team import Team

def get_team_composition_stats(team: Team):
    composition_stats = {
        'throwers': [],
        'halfs': [],
        'clevers': [],
        'aggressives': [],
        'evasives': [],
    }
    
    for pastTeam in team.team_composition_history:
        cleverCt = 0
        throwerCt = 0
        halfCt = 0
        aggressiveCt = 0
        evasiveCt = 0
        for player in pastTeam:
            if isinstance(player, Clever):
                cleverCt += 1
            elif isinstance(player, Thrower):
                throwerCt += 1
            elif isinstance(player, Half):
                halfCt += 1
            elif isinstance(player, Aggressive):
                aggressiveCt += 1
            elif isinstance(player, Evasive):
                evasiveCt += 1
        composition_stats['throwers'].append(throwerCt)
        composition_stats['halfs'].append(halfCt)
        composition_stats['clevers'].append(cleverCt)
        composition_stats['aggressives'].append(aggressiveCt)
        composition_stats['evasives'].append(evasiveCt)
    
    return composition_stats

def plotWins (t1: Team, t2: Team, t1_wins, t2_wins):
    comp1 = get_team_composition_stats(t1)
    comp2 = get_team_composition_stats(t2)
    
    
    plt.subplot(1,2,1)
    sns.lineplot(data = t1_wins, label='team 1')
    sns.lineplot(data = t2_wins, label='team 2')
    plt.title(f"wins per team over {len(t1_wins)} game plays")
    plt.legend()
    plt.ylabel('wins')
    plt.xlabel('number of games')

    plt.subplot(1,2,2)
    sns.lineplot(data = comp1['throwers'], label= "# of throwers")
    sns.lineplot(data = comp1['halfs'], label= "# of halfs")
    sns.lineplot(data = comp1['clevers'], label= "# of clevers")
    sns.lineplot(data = comp1['aggressives'], label= "# of aggressives")
    sns.lineplot(data = comp1['evasives'], label= "# of evasives")
    
    plt.legend()
    plt.title('number of each playertype at each simulated game')
    plt.ylabel('players')
    plt.xlabel('number of games')
    plt.show()

    print('throwers', comp1['throwers'][-1])
    print('halfs', comp1['halfs'][-1])
    print('clevers', comp1['clevers'][-1])
    print('aggressives', comp1['aggressives'][-1])
    print('evasives', comp1['evasives'][-1])