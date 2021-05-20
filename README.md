# Two Player Zero-Sum-Games-Equilibrium

- Minimax equilibrium
- All Pure Strategy Nash Equilibriums
- Mixed Strategy Nash Equilibrium

### Libraries Used:
- numpy
- cvxpy

### Usage:
- `/run <input_file> <output_file>` or `python3 main.py <input_file> <output_file>` 

### PSNE

Algorithm for finding all the PSNE:
- Fix a strategy(a1) from the strategy space of player1, Find all the possible strategies(b1) of player2, which maximizes its utility when Player1 chooses a1. [strategy (a1,b1)]
- Repeat this by fixing each strategy of player1 and collect all such strategy profiles into set S1.
- Similarly, Collect all the strategy profiles by fixing actions of player2 and finding the strategies of player1 for the action chosen by player2 into set S2.
- The intersection of sets S1 and S2 gives the strategies in Pure Strategy Nash Equilibrium. 

#### Time Complexity
- Polynomial time algorithm. O(n*m), where n, m are no.of strategies of player1 and player2.

### Minimax

Linear Formulation and Linear solver is used for finding a minimax equilibrium. Since this is Two player zero-sum game the minimax equilibrium is same as MSNE.
- Let (p1,p2,...pn), (q1,q2,...qn) be the probabilities with which player1, player2 chooses his strategies.
- aij be the utility of player1 when player1 and player2 choose their ith and jth actions, respectively.
- The LP formulation for player1 is as follows:
    - `max Z`
    - `Z - sum(aij*pi) <= 0` forall `j` in `[n]`
    - `sum(pi) = 1`
    - `pi >= 0` forall `i`
- Similarly, we formulate LP for player2 as follows:
    - `min W`
    - `sum(aij*qi) - W <= 0` forall `j` in `[n]`
    - `sum(qi) = 1`
    - `qi >= 0` forall `i`

#### Time Complexity
- Polynomial time algorithm. O(n+m), where n is no.of strategies of player1 and m is no.of strategies of player2.
