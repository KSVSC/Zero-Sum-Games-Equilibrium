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
            print("file provided is not in correct format")
            exit(1)
        self.data = open(file_name, "r").readlines()
        temp = [word for word in self.data[1].strip().split("}") if len(word) != 0]  # players names and number of strategies
        self.ply_names = temp[0].strip('{ "').split('" "')
        self.num_plys = len(self.ply_names)
        self.plys_num_strats = [int(num) for num in temp[1].strip('{ "').split(' ')]
        if self.num_plys != len(self.plys_num_strats):
            print("number of players and number of strategies for players are not matching")
            exit(1)
        self.parse_game()

    def parse_game(self):
        self.ply_map = dict()
        self.utility = np.zeros(tuple(self.plys_num_strats + [self.num_plys]))
        for i, name in enumerate(self.ply_names):
            self.ply_map[name] = Player(name, i, self.plys_num_strats)
        score = [float(num) for num in self.data[3].strip().split(" ")]
        if len(score) != np.prod(self.plys_num_strats)*self.num_plys:
            print("number of utilities given doesn't match the requirement")
            exit(1)
        # denotes index in utility map for each player
        ind_arr = np.zeros(self.num_plys, dtype=int)
        i = 0  # index for iterating over utility values of all players
        while i < len(score):
            # print("ind_arr", ind_arr)
            for n, name in enumerate(self.ply_names):
                self.ply_map[name].utility[tuple(ind_arr)] = score[i]
                self.utility[tuple(ind_arr)+tuple([n])] = score[i]
                i = i+1
            # helps is changing the strategy for a player
            j = int(i/self.num_plys)
            for k, _ in enumerate(ind_arr):
                ind_arr[k] = j % self.plys_num_strats[k]
                j = int(j / self.plys_num_strats[k])
            # print("map", self.ply_map)
            # print("utility",self.utility)

        # for k, v in self.ply_map.items():  # printing to test utility maps of all players
        #     print(k)
        #     print(v.utility)

        print(self.utility)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage : python3 main.py input_filename")
        exit(1)
    game = Game(sys.argv[1])
