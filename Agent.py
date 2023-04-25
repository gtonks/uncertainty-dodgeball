import numpy as np

class Agent:

    def __init__(self, nPlayers, eps):
        self.nPlayers = nPlayers
        self.eps = eps
        self.n = np.zeros(nPlayers) # player counts n(a)
        self.Q = np.zeros(nPlayers) # value Q(a)

    def update_Q(self, player, reward):
        # Update Q action-value given (action, reward)
        self.n[player] += 1
        self.Q[player] += (1.0/self.n[player]) * (reward - self.Q[player])
        # print(self.Q)

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps: # explore
            return np.random.choice(self.nPlayers)
        else: # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))