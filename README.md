# uncertainty-dodgeball
CS5060 Final Project: Dodgeball Simulation

This repository contains code to run a simplified simulation of a game of dodgeball. It aims to answer the question of how to choose a team with an optimal mix of players, based on their different strateigies. This simulation uses the the principles of game theory and explore and exploit to discover the optimal strategy by playing the game many times until a stable strategy is found.

The game pits two teams against each other, which are constructed by two different "coaches" (the agents in our simulation).

## How a game works
Each round, a player (Agent) goes to a random Location. (The number of locations is a parameter that can be configured as part of the simulation, but by default is set to continually match the number of players currently in a team.) The player chooses one of three actions to perform:
- DODGE: This prevents a player from getting hit and leaving the game for that round.
- PICK_UP: Each round, one player at each Location who chooses this action will get a ball.
- THROW: If the player has a ball, he randomly chooses someone from the other team at that Location to throw a ball at. If the targeted player did not dodge, he is eliminated. Regardless of outcome, the player who chose this action no longer has a ball.

Rounds continue until every player on a team is eliminated. The team with players remaining wins.

## Simulation Flow
At the end of a game, coaches will evaluate the performance of their team and make changes to the team based on their strategy. Initially, teams will start with 1 player each. Teams will add additional players after each game.

Team sizes are limited to a specific number of players, configurable as part of the simulation. Once teams have reached the configured size, players will be swapped out depending on the policy of the coach to try to find a more optimal team composition.

## The Coaches

The two different coaches take two different approaches to how they construct their teams. The first coach is the one we are interested in as the second serves as more of a baseline to drive the first coach's strategy.

### Coach 1: Explore and Exploit

This coach uses the principles of explore and exploit to construct his team. He uses an epsilon-greedy algorithm to determine what type of player to add/swap-in to the team based on the previous performance they have had in the game. When swapping out, this coach will always swap out the player type with the lowest performance.

### coach 2: Random

This coach just works off of randomly selecting players to add/swap-in to the team. This coach is used as a baseline to compare the performance of the first coach to and serves as a way to test if coach 1's strategy is really any good at all.

## Player specifications
### Thrower
This player never dodges. If he has a ball, he throws it. Otherwise, he attempts to pick up a ball.

### Half
This player dodges half of the time. The rest of the time, he functions like a Thrower.

### Clever
This player knows the fraction of players on the other team that have balls. When more than half of them do, he dodges. He functions like a Thrower the rest of the time.

### Aggressive
Aggressive players are very similar to the thrower in that they play more offensively. However, instead of always throwing, they will choose to throw 75% of the time and will choose to dodge 25% of the time.

### Evasive
Evasive players tend to play it a bit more on the safe side, trying to avoid more than they throw. Evasive players will choose to dodge 65% of the time, and throw 35% of the time.

## Running the Code

Our program has a number of dependencies that need to be installed to run this program:

- Numpy
- Seaborn
- Matplotlib
- Pandas

These dependencies can be installed using `pip` or `conda`. Any recent version of these libraries should work, though a `requirements.txt` file has also been provided for convienience with the versions of the libraries we used to develop this program.

The main entrypoint of the program is `main.py`. No parameters are passed on the command line. The program will run the simulation and ouuput the progress in the console and will display a summary graph at the end of the simulation run. After ensuring the required dependencies are installed, simply run the program with the following command from the root of the repository with Python 3 installed:

```
python main.py
```

## Adjusting the Simulation Parameters
The simulation has a number of parameters that can be adjusted to change the behavior of the simulation. These parameters can be adjusted by changing the variables declared at the top of the `simulate()` function found in `main.py`. The following parameters can be adjusted:

- Number of game rounds to simulate
- Maximum number of players on a team
- The epsilon value used by coach 1 in their epsilon-greedy strategy.
- Number of locations available to players
  - Note that to adjust this parameter, presently, some lines have to be commented-out and uncommented to set the simulation to honor a user-specified value. See the comments in the `simulate()` function of `main.py` for further details.
- Initial team composition
  - By default, we initialize the game with empty teams. If you want to start with some initial team, you can specify initial players in the lists passed to the `Team` constructors in `main.py`'s `simulate()` function.
