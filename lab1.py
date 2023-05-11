#!/usr/bin/python3.12
import math
import numpy
from typing import Callable


def bisection_method(func: Callable[[float], float], a: float, b: float, eps: float):
    if numpy.sign(func(a)) == numpy.sign(func(b)):
        return None

    midpoint = (a + b) / 2

    if numpy.abs(func(midpoint)) < eps:
        return midpoint, func(midpoint)
    elif numpy.sign(func(a)) == numpy.sign(func(midpoint)):
        return bisection_method(func, midpoint, b, eps)
    else:
        return bisection_method(func, a, midpoint, eps)


def main():
    func: Callable[[float], float] = lambda x: math.sin(x ** 2 - x + (1 / 3)) + x / 2

    print("Please determine the beginning of the range")
    xb = float(input())
    print("Please determine the end of the range")
    xe = float(input())
    print("Please determine the accuracy")
    eps = float(input())
    root, value = bisection_method(func, xb, xe, eps)
    print("Root: ", root, " Value: ", value)


if __name__ == '__main__':
    main()
