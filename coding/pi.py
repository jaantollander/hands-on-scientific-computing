#!/usr/bin/env python3
from decimal import Decimal, getcontext
from math import factorial
import argparse
import random


def chudnovsky(precision):
    getcontext().prec = precision + 1
    C = 426880*Decimal(10005).sqrt()
    M = Decimal(1)
    L = 13591409
    s = 13591409
    X = Decimal(1) 
    K = Decimal(6)
    
    for i in range(0, precision):
        M *= (K**3 - 16*K) / ((i + 1)**3)
        X *= 262537412640768000
        L += 545140134
        K += 12
        s += Decimal((M*L)/X)

    pi = C/s
    return pi


def is_in_circle(x, y):
    return x**2 + y**2 < 1

def points_in_circle(iterations, seed):
    gen = random.Random(seed)
    in_circle_points = 0
    for _ in range(iterations):
        x = gen.uniform(0, 1)
        y = gen.uniform(0, 1) 
        if is_in_circle(x, y):
            in_circle_points += 1
    return in_circle_points

def monte_carlo_pi(iterations, seed):
    pi = points_in_circle(iterations, seed)*4/iterations
    return pi


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'precision', type=int, help="Number of Pi digits")
    parser.add_argument(
            'iters', type=int, help="Number of iterations")
    parser.add_argument(
            '--seed', type=int, help="Random seed", default=42)

    args = parser.parse_args()

    precision = args.precision
    iterations = args.iters
    seed = args.seed

    print("Using the Chudnovsky algorithm, Pi is {}" \
         " with {} digits after the decimal point.".format(chudnovsky(precision), precision))

    print("Using the monte carlo algorithm, Pi is {} with {} iterations" \
        " and seed value {}.".format(monte_carlo_pi(iterations, seed), iterations, seed))
