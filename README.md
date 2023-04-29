# uncertainty-dodgeball
CS5060 Final Project: Dodgeball Simulation

## How a game works
Each round, a player (Agent) goes to a random Location. The player chooses one of three actions to perform:
- DODGE: This prevents a player from getting hit and leaving the game for that round.
- PICK_UP: Each round, one player at each Location who chooses this action will get a ball.
- THROW: If the player has a ball, he randomly chooses someone from the other team at that Location to throw a ball at. If the targeted player did not dodge, he is eliminated. Regardless of outcome, the player who chose this action no longer has a ball.

Rounds continue until every player on a team is eliminated. The team with players remaining wins.

## Player specifications
### Thrower
This player never dodges. If he has a ball, he throws it. Otherwise, he attempts to pick up a ball.

### Half
This player dodges half of the time. The rest of the time, he functions like a Thrower.

### Clever
This player knows the fraction of players on the other team that have balls. When more than half of them do, he dodges. He functions like a Thrower the rest of the time.
