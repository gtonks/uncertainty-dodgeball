class Environment:

    def __init__(self, probs):
        self.probs = probs  # success probabilities for each arm

    def step(self, winner):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        # return 1 if winner > 0 else 0
        return winner