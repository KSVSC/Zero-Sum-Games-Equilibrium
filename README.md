# Two Player Zero-Sum-Games-Equilibrium

- Minimax equilibrium
- All Pure Strategy Nash Equilibriums
- Mixed Strategy Nash Equilibrium

### Libraries Requirements:
- numpy
- cvxpy

### Usage:
- /run <input_file> <output_file>

### PSNE

To find all PSNE the following algorithm used:
- Fix an action(a1) from the action set of player1, Find all the actions(b1) from the action set of player2 which gives him maximum utility when Player1 chooses a1. [strategy (a1,b1)]
- Do this by fixing every action of player1 and find the strategies of player2 which gives maximum utility for the player1's choosen action.
- Collect all such strategies into set S1.
- Similarly, Collect all the strategies by fixing actions of player2 and finding the strategies of player1 for the action choosen by player2 into set S2.
- Now, Find the intersection of sets S1 and S2.
- The strategies in the intersection are in equilibrium. Since all the strategies are single actions it is Pure Strategy Nash Equilibrium.

#### Time Complexity
- Polynomial time algorithm. O(n*m), where n is no.of strategies of player1 and m is no.of strategies of player2.

### Minimax

Linear Formulation and Linear solver is used for finding a minimax equilibrium. Since this is TWo player zero-sum game the minimax equilibrium is same as MSNE.
- Let (p1,p2,..pn) be the probabilities with which player1 chooses his actions.
- aij be the utility of player1 when ith action is choosen by player1 and jth action is choosen by player2.
- z be the utility player1 tries to maximize.
- The LP formulation for player1 is as follows:
    - max Z
    - z - sum(aij*pi) <= 0 forall j in [n]
    - sum(pi) = 1
    - pi >= 0 forall i
- Let (q1,q2,..qn) be the probabilities with which player2 chooses his actions.
- -aij be the utility of player2 when ith action is choosen by player1 and jth action is choosen by player2.
- -w be the utility player1 tries to maximize.
- The LP formulation for player2 is as follows:
    - min w
    - sum(aij*qi) - w <= 0 forall j in [n]
    - sum(qi) = 1
    - qi >= 0 forall i

#### Time Complexity
- Polynomial time algorithm. O(n+m), where n is no.of strategies of player1 and m is no.of strategies of player2.