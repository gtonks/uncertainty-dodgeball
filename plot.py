import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plotWins (team1, team2, desc):
    
    sns.lineplot(data = team1, label='team 1')
    sns.lineplot(data = team2, label='team 2')

    plt.title(desc)
    plt.legend()
    plt.ylabel('wins')
    plt.xlabel('number of games')
    plt.show()