
from itertools import combinations
import time


def timeit(f):
    def helper(*args):
        start = time.time()
        result = f(*args)
        finish = time.time()
        print("It took {} seconds to process.".format(finish-start))
        return result
    return helper





class GameHandler:

    def __init__(self, players):
        self.players = players
        self.K = 32
        self.tao = .4

    ## @timeit
    def round_robin(self, num_rounds):
        for i in range(num_rounds):
            for pair in combinations(self.players, 2):
                self.one_game(pair[0], pair[1])
        for player in self.players:
            player.calculate_glick(self.tao)
        for player in self.players:
            player.update_glick()
        self.print_standings()

    def print_standings(self):
        ## self.players.sort(key=lambda x: x.elo)
        for player in self.players:
            print("{} : {} : {} : {} : {}".format(player.name, round(player.elo, 0),
                  round(player.glick, 0), round(player.g_deviation, 2), player.g_volatility))

    def one_game(self, player1, player2):
        player1.opponents.append(player2)
        player2.opponents.append(player1)
        p1_score = player1.get_score()
        p2_score = player2.get_score()
        if p1_score > p2_score:
            self.adjust_elo(player1, player2)
            player1.record.append(1)
            player2.record.append(0)
        if p1_score < p2_score:
            self.adjust_elo(player2, player1)
            player1.record.append(0)
            player2.record.append(1)
        if p1_score == p2_score:
            self.adjust_elo(player1, player2, True)
            player1.record.append(0.5)
            player2.record.append(0.5)

    def adjust_elo(self, winner, loser, tie=False):
        winner_expected = 1 / (1 + 10 ** ((loser.elo - winner.elo) / 400))
        loser_expected = 1 - winner_expected
        if not tie:
            winner.update_elo(self.K * (1 - winner_expected))
            loser.update_elo(self.K * (-loser_expected))
        else:
            winner.update_elo(self.K * (0.5 - winner_expected))
            loser.update_elo(self.K * (0.5 - loser_expected))

    def reset(self):
        for player in self.players:
            player.elo = 1000



