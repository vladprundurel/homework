from common_mpmath import f, INTERVALS, MAX_ITERATIONS, EPSILON, same_sign
from mpmath import *

def fderiv(x):
    return mpf(36) * e**(-x) * sqrt(x) * cos(mpf(6) * x**(mpf(3/2)))- mpf(4) * e**(-x) * sin(mpf(6) * x**(mpf(3/2)))

def get_root(interval):
    x_n = mpf((interval[0] + interval[1]) / 2)

    step = 0
    while step < MAX_ITERATIONS:
        step += 1

        x_n_plus_1 = x_n - f(x_n) / fderiv(x_n) / 10 # fix for last term

        if x_n_plus_1 < interval[0] or interval[1]  < x_n_plus_1:
            print("wtf", x_n_plus_1, interval)

        if abs(f(x_n_plus_1)) < EPSILON:
            return x_n_plus_1

        x_n = x_n_plus_1

def correct_interval(interval):
    return not same_sign(f(interval[0]), f(interval[1]))

for interval in INTERVALS:
    if correct_interval(interval):
        print(interval, get_root(interval))
