
import numpy as np
from numpy import random


def multiply(x, y, z):
    return x * y * z

def special_function(x, k, tao, delta, g_dev, v, a):
    return np.exp(x - k * tao) * (delta ** 2 - g_dev ** 2 - v - np.exp(x - k * tao)) / \
           (2 * (g_dev ** 2 + v + np.exp(x - k * tao))) - ((x - k * tao - a) / (tao ** 2))



class Player:

    def __init__(self, name, mean, sd):
        self.elo = 1000
        self.glick = 1500
        self.g_deviation = 350
        self.g_volatility = 0.06
        self.new_glick = None
        self.new_g_dev = None
        self.new_g_vol = None
        self.name = name
        self.mean = mean
        self.sd = sd
        self.opponents = []
        self.record = []




    def get_score(self):
        return random.normal(self.mean, self.sd)

    def update_elo(self, change):
        self.elo += change

    def calculate_glick(self, tao):
        mu = (self.glick - 1500) / 173.7178
        phi = self.g_deviation / 173.7178
        opps_glick = []
        opps_dev = []
        for opp in self.opponents:
            opps_glick.append((opp.glick - 1500) / 173.7178)
            opps_dev.append(opp.g_deviation / 173.7178)
        func_of_phi = []
        func_E = []
        sum_terms = []
        delta_sum_terms = []

        for i in range(len(self.opponents)):
            func_of_phi.append(1 / np.sqrt(1 + 3 * (opps_dev[i] ** 2) / (np.pi ** 2)))

            func_E.append(1 / (1 + np.exp(-func_of_phi[i] * (mu - opps_glick[i]))))

            sum_terms.append((func_of_phi[i] ** 2) * func_E[i] * (1 - func_E[i]))
            delta_sum_terms.append(func_of_phi[i] * (self.record[i] - func_E[i]))
        v = 1 / sum(sum_terms)
        delta = v * sum(delta_sum_terms)

        a = np.log(self.g_volatility ** 2)
        A = a
        if delta ** 2 > phi ** 2 + v:
            B = np.log(delta ** 2 - phi ** 2 - v)
        else:
            k = 1
            while special_function(a, k, tao, delta, phi, v, a) < 0:
                k += 1
            B = (a - k * tao)
        FA = special_function(A, 0, tao, delta, phi, v, a)
        FB = special_function(B, 0, tao, delta, phi, v, a)

        while abs(A - B) > 0.000001:

            C = A + (A - B) * (FA / (FB - FA))
            FC = special_function(C, 0, tao, delta, phi, v, a)
            if FC * FB < 0:
                A = B
                FA = FB
            else:
                FA = FA / 2
            B = C
            FB = FC

        self.new_g_vol = np.exp(A / 2)
        phi_star = np.sqrt(phi ** 2 + self.new_g_vol ** 2)
        self.new_g_dev = (1 / np.sqrt((1 / phi_star ** 2) + (1 / v))) * 173.7178
        self.new_glick = (mu + (self.new_g_vol ** 2) * sum(delta_sum_terms)) * 173.7178 + 1500


    def update_glick(self):
        self.glick = self.new_glick
        self.g_deviation = self.new_g_dev
        self.g_volatility = self.new_g_vol


