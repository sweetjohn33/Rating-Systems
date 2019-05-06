from numpy import random


class Player:

    def __init__(self, name, mean, sd):
        self.elo = 1000
        self.name = name
        self.mean = mean
        self.sd = sd


    def get_score(self):
        return self.mean + random.normal(self.mean, self.sd)

    def update_elo(self, change):
        self.elo += change
