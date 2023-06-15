import math
from typing import Callable

import numpy


def bisection_method(
        func: Callable[[float], float],
        range_start: float,
        range_end: float,
        epsilon: float
) -> float:
    if numpy.sign(func(range_start)) == numpy.sign(func(range_end)):
        raise ValueError()

    i = 0
    while True:
        midpoint = (range_start + range_end) / 2
        i += 1
        if numpy.abs(func(midpoint)) <= epsilon:
            print(f"Iteration {i}: {midpoint} - Criteria met!")
            return midpoint
        else:
            print(f"Iteration {i}: {midpoint}")

        if numpy.sign(func(range_start)) == numpy.sign(func(midpoint)):
            range_start = midpoint
        else:
            range_end = midpoint


def main() -> None:
    func: Callable[[float], float] = lambda x: 2 * math.log(x + 3) - 4

    xb = -2
    xe = 8
    eps = 0.0001

    root = bisection_method(func, xb, xe, eps)
    print(f"Root: {root}")


if __name__ == '__main__':
    main()
