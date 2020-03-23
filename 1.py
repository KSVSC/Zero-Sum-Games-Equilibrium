import numpy as np
import sys
import itertools


class Player:
    '''
    player will has his utility matrix
    '''
    def __init__(self, name, ind, total_strats):
        self.name = name
        self.ind = ind
        self.num_strats = total_strats[ind]
        self.utility = np.ndarray(total_strats)  # utility map for that player

class Game:
    def __init__(self, file_name):
        '''gets players names and number of strategies'''
        if len(file_name.split('.')) != 2 or file_name.split('.')[1] != "nfg":
            print("File provided is not in correct format")
            exit(1)
        self.data = open(file_name, "r").readlines()
        temp = [word for word in self.data[1].strip().split("}") if len(word) != 0]  # players names and number of strategies
        self.ply_names = temp[0].strip('{ "').split('" "')
        self.num_plys = len(self.ply_names)
        if self.num_plys != 2:
            print("Input given is not Two-player game")
            exit(1)
        self.plys_num_strats = [int(num) for num in temp[1].strip('{ "').split(' ')]
        if self.num_plys != len(self.plys_num_strats):
            print("Number of players and number of strategies for players are not matching")
            exit(1)
        self.parse_game()

    def parse_game(self):
        self.ply_map = dict()
        self.utility = np.zeros(tuple(self.plys_num_strats + [self.num_plys]))
        for i, name in enumerate(self.ply_names):
            self.ply_map[name] = Player(name, i, self.plys_num_strats)
        score = [float(num) for num in self.data[3].strip().split(" ")]
        if len(score) != np.prod(self.plys_num_strats)*self.num_plys:
            print("Number of utilities given doesn't match the requirement")
            exit(1)
        # denotes index in utility map for each player
        ind_arr = np.zeros(self.num_plys, dtype=int)
        i = 0  # index for iterating over utility values of all players
        while i < len(score):
            for n, name in enumerate(self.ply_names):
                self.ply_map[name].utility[tuple(ind_arr)] = score[i]
                self.utility[tuple(ind_arr)+tuple([n])] = score[i]
                i = i+1
            # helps is changing the strategy for a player
            j = int(i/self.num_plys)
            for k, _ in enumerate(ind_arr):
                ind_arr[k] = j % self.plys_num_strats[k]
                j = int(j / self.plys_num_strats[k])

        for i in range(self.plys_num_strats[0]):
            for j in range(self.plys_num_strats[1]):
                if sum(self.utility[i, j]) != 0:
                    print("Input given is not zero sum game")
                    exit(1)
        # print(self.utility)
        self.PSNE()

    def PSNE(self):
        a1 = []
        for i in range(self.plys_num_strats[1]):
            max_util = np.amax(self.utility[:, i, 0])
            idx = np.where(self.utility[:, i, 0] == max_util)
            for j in range(len(idx[0])):
                a1.append((idx[0][j], i))
        a2 = []
        for i in range(self.plys_num_strats[0]):
            max_util = np.amax(self.utility[i, :, 1])
            idx = np.where(self.utility[i, :, 1] == max_util)
            for j in range(len(idx[0])):
                a2.append((i, idx[0][j]))
        a1 = set(a1)
        a2 = set(a2)
        e = list(a1.intersection(a2))
        e.sort()
        print(len(e))
        for i in range(len(e)):
            print(e[i][0], e[i][1])
    
    def minimax(self):
        #Fetching the utilities for row player
        utils = np.reshape(self.utility,(np.prod(self.plys_num_strats), self.num_plys))
        # utils2 is the matrix representation of the game containing utilities for player1
        # dim(utils) = player1strats x player2strats 
        utils2 = np.reshape(utils[:,0], self.plys_num_strats)

        row_player_strat = cp.Variable(self.plys_num_strats[0])
        col_player_strat = cp.Variable(self.plys_num_strats[1])
        row_util = cp.Variable()
        col_util = cp.Variable()


        constraints1 = [row_player_strat >= 0, row_player_strat <= 1]
        constraints2 = [col_player_strat >= 0, col_player_strat <= 1]

        constraints1.append(cp.sum(row_player_strat) == 1)
        constraints2.append(cp.sum(col_player_strat) == 1)

        for row_ply_turn in utils2:
            for i in range(len(row_ply_turn)):
                temp = col_player_strat[i] * row_ply_turn[i]
            constraints2.append(row_util - temp >= 0)

        for col_ply_turn in utils2.T:
            for i in range(len(col_ply_turn)):
                temp = row_player_strat[i] * col_ply_turn[i]
            constraints1.append(col_util + temp <= 0)
        
        obj1 = cp.Maximize(row_util)
        obj2 = cp.Minimize(col_util)

        problem1 = cp.Problem(obj1, constraints1)
        problem2 = cp.Problem(obj2, constraints2)

        problem1.solve()
        problem2.solve()

        print(problem1.status)
        print(problem2.status)   


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage : python3 main.py input_filename")
        exit(1)
    game = Game(sys.argv[1])
