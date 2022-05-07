""" Tentative code.
"""


import numpy as np
import scipy.integrate
import math

# Interpreting z(t) into the integral to get P, gives:
# P = c1(c2(e^c2*y(0) -e^c2*y(-T) -T)

coefs = {'male': {'c1': 10.1817,
                  'c2': 5.7808,
                  'c3': 41.9374,
                  'c4': 9.8382},
         'female': {'c1': 9.8556,
                    'c2': 5.0167,
                    'c3': 34.2325,
                    'c4': 9.7581}}


def get_normalized_yt(yt, ymax, y_threshold):
    out = (yt - y_threshold) / (ymax - y_threshold)
    if out < 0:
        return 0
    if out > 1:
        return 1
    return out


def get_z_t(yt0, yt_t, t, gender='male'):
    return coefs[gender]['c1'] * \
           (coefs[gender]['c2'] *
            (math.exp(coefs[gender]['c2'] * yt0) - (math.exp(coefs[gender]['c2'] * yt_t)))
            - t)


def calculate_v(P, gender='male'):
    return coefs[gender]['c3'] + coefs[gender]['c4'] * (1 - np.exp(-P))


def main(yt, ymax, y_threshold):
    norm = list()
    for i in yt:
        norm.append(get_normalized_yt(i, ymax, y_threshold))
    print(norm)
    out2 = list()
    for i in norm:
        out2.append(get_z_t(i))
    print(out2)
    for i in out2:
        print(calculate_v(i))
    return scipy.integrate.quad(get_z_t, -7, 0)


if __name__ == '__main__':
    act = []
    d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0
    y_th = 143
    d7 = [140, 150, 150, 163, 150, 90]
    act = [d1, d2, d3, d4, d5, d6] + d7
    ymx = max(d7)
    print(main(act, ymx, y_th))

