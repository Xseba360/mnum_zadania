import math
from collections import OrderedDict

import numpy


def lagrange_interpolation(data: OrderedDict[float, float], x: float) -> float:
    result = 0.0
    x_values = [key for key in data]
    f_values = [data[key] for key in data]
    n = len(x_values)

    for i in range(n):
        term = f_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


def main() -> None:
    data: OrderedDict[float, float] = OrderedDict({
        -1.5: -0.69,
        -1.0: 0.0,
        0.0: 0.69,
        1.0: 1.09,
        2.0: 1.38,
        5.0: 1.95,
    })

    start_x = min(data.keys())
    end_x = max(data.keys())

    delta = 0.5

    for x in numpy.arange(start_x, end_x + delta, delta):
        f_exact = math.log(x + 2)
        f_approx = lagrange_interpolation(data, x)
        print(f'x = {x:.1f},\tW(x) = {f_approx:.10f},\tf(x) = {f_exact:.10f}')


if __name__ == '__main__':
    main()
