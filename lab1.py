#!/usr/bin/python3.12
import math
import numpy
from typing import Callable


def bisection_method(
        func: Callable[[float], float],
        range_start: float,
        range_end: float,
        epsilon: float
) -> float:
    if numpy.sign(func(range_start)) == numpy.sign(func(range_end)):
        raise ValueError()

    midpoint = (range_start + range_end) / 2

    if numpy.abs(func(midpoint)) < epsilon:
        return midpoint
    elif numpy.sign(func(range_start)) == numpy.sign(func(midpoint)):
        return bisection_method(func, midpoint, range_end, epsilon)
    else:
        return bisection_method(func, range_start, midpoint, epsilon)


def newton_method(
        funcs: list[Callable[[float], float]],
        range_start: float,
        range_end: float,
        epsilon: float
) -> float:
    if numpy.sign(funcs[0](range_start)) == numpy.sign(funcs[0](range_end)):
        raise ValueError()

    x0 = (range_start + range_end) / 2
    x1 = x0 - funcs[0](x0) / funcs[1](x0)

    while numpy.abs(x1 - x0) >= epsilon:
        x0 = x1
        x1 = x0 - funcs[0](x0) / funcs[1](x0)

    return x1


def secant_method(
        func: Callable[[float], float],
        range_start: float,
        range_end: float,
        epsilon: float
) -> float:
    x0 = (range_start * func(range_end) - range_end * func(range_start)) / (func(range_end) - func(range_start))

    f0 = func(x0)

    while numpy.abs(f0) >= epsilon:
        x0 = (range_start * func(range_end) - range_end * func(range_start)) / (func(range_end) - func(range_start))
        f0 = func(x0)
        fp = func(range_start)
        if f0 * fp > 0:
            range_start = x0
        else:
            range_end = x0
    return x0


def main() -> None:
    func: Callable[[float], float] = lambda x: math.sin(x ** 2 - x + (1 / 3)) + x / 2

    func2: Callable[[float], float] = lambda x: \
        ((x + x) - 1) * \
        math.cos(x ** 2 - x + (1 / 3)) + 1 / 2

    func3: Callable[[float], float] = lambda x: \
        2 * math.cos(x ** 2 - x + (1 / 3)) - \
        (((x + x) - 1) ** 2) * \
        math.sin(x ** 2 - x + (1 / 3))

    print("Please determine the beginning of the range")
    xb = float(input())
    print("Please determine the end of the range")
    xe = float(input())
    print("Please determine the accuracy")
    eps = float(input())

    # xb = -3
    # xe = 1
    # eps = 0.0001

    print("Bisection method:")
    root = bisection_method(func, xb, xe, eps)
    print("Root: ", root)

    print("Newton's method:")
    root2 = newton_method([
        func,
        func2,
        func3
    ], xb, xe, eps)
    print("Root: ", root2)

    print("Secant method:")
    root3 = secant_method(func, xb, xe, eps)
    print("Root: ", root3)


if __name__ == '__main__':
    main()
