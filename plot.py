import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Half import Half
from Thrower import Thrower
from Clever import Clever
def plotWins (t1, t2, t1_wins, t2_wins):
    
    comp1 = [[],[],[]]
    comp2 = [[],[],[]]
    
    throwers1 = 0
    throwers2 = 0
    halfs1 = 0
    halfs2 = 0
    clevers1 = 0
    clevers2 = 0
    for i in range(len(t1.players)):
        if isinstance(t1.players[i], Clever):
            clevers1 += 1
        elif isinstance(t1.players[i], Thrower):
            throwers1 += 1
        else:
            halfs1 +=1

        if isinstance(t2.players[i], Clever):
            clevers2 += 1
        elif isinstance(t2.players[i], Thrower):
            throwers2 += 1
        else:
            halfs2 +=1

        comp1[0].append(throwers1)
        comp1[1].append(halfs1)
        comp1[2].append(clevers1)
        
        comp2[0].append(throwers2)
        comp2[1].append(halfs2)
        comp2[2].append(clevers2)

    plt.subplot(1,2,1)
    sns.lineplot(data = t1_wins, label='team 1')
    sns.lineplot(data = t2_wins, label='team 2')
    plt.title(f"wins per team growing over {len(t1_wins)} plays")
    plt.legend()
    plt.ylabel('wins')
    plt.xlabel('number of games')

    plt.subplot(1,2,2)
    sns.lineplot(data = comp1[0], label= "# of throwers")
    sns.lineplot(data = comp1[1], label= "# of halfs")
    sns.lineplot(data = comp1[2], label= "# of clevers")
    
    plt.legend()
    plt.title('number of each playertype as games win/lose')
    plt.ylabel('players')
    plt.xlabel('number of games')
    plt.show()

    print('throwers', comp1[0][-1])
    print('halfs', comp1[1][-1])
    print('clevers', comp1[2][-1])