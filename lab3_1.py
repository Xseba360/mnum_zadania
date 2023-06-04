from collections import OrderedDict
from typing import Tuple


def calculate_determinants(data: OrderedDict[float, float]) -> Tuple[float, float, float, float]:
    n = len(data) - 1
    sum_x4 = sum(x ** 4 for x in data.keys())
    sum_x3 = sum(x ** 3 for x in data.keys())
    sum_x2 = sum(x ** 2 for x in data.keys())
    sum_x = sum(data.keys())
    sum_fx2 = sum(fx * x ** 2 for x, fx in data.items())
    sum_fx = sum(fx * x for x, fx in data.items())
    sum_f = sum(data.values())

    determinant_g = (
            sum_x4 * sum_x2 * (n + 1)
            + sum_x3 * sum_x * sum_x2
            + sum_x2 * sum_x3 * sum_x
            - sum_x2 ** 3
            - sum_x ** 2 * sum_x4
            - sum_x3 ** 2 * (n + 1)
    )

    determinant_a = (
            sum_fx2 * sum_x2 * (n + 1)
            + sum_fx * sum_x * sum_x2
            + sum_f * sum_x3 * sum_x
            - sum_f * sum_x2 ** 2
            - sum_x ** 2 * sum_fx2
            - sum_fx * sum_x3 * (n + 1)
    )

    determinant_b = (
            sum_x4 * sum_fx * (n + 1)
            + sum_x3 * sum_f * sum_x2
            + sum_x2 * sum_fx2 * sum_x
            - sum_fx * sum_x2 ** 2
            - sum_x4 * sum_f * sum_x
            - sum_x3 * sum_fx2 * (n + 1)
    )

    determinant_c = (
            sum_x4 * sum_x2 * sum_f
            + sum_x3 * sum_x * sum_fx2
            + sum_x2 * sum_x3 * sum_fx
            - sum_x2 ** 2 * sum_fx2
            - sum_x4 * sum_x * sum_fx
            - sum_x3 ** 2 * sum_f
    )

    return determinant_g, determinant_a, determinant_b, determinant_c


def main() -> None:
    data: OrderedDict[float, float] = OrderedDict({
        -4.0: 4.0,
        -3.0: 2.25,
        -2.0: 1.0,
        -0.6: 0.25,
        -0.2: 0.0,
        1.0: 1.0,
        3.0: 2.25,
        6.0: 4.0,
        7.0: 6.25,
    })

    determinant_g, determinant_a, determinant_b, determinant_c = calculate_determinants(data)

    result_a = determinant_a / determinant_g
    result_b = determinant_b / determinant_g
    result_c = determinant_c / determinant_g

    print("General determinant:", determinant_g)
    print()
    print("Determinant a:", determinant_a)
    print("Determinant b:", determinant_b)
    print("Determinant c:", determinant_c)
    print()
    print("Result a:", result_a)
    print("Result b:", result_b)
    print("Result c:", result_c)
    print()
    print("Approximation:")
    print("x", "\t", "f", "\t", "ax^2+bx+c")

    for x_val, f_val in data.items():
        approximation = result_a * x_val ** 2 + result_b * x_val + result_c
        print("{:n}".format(x_val), "\t", "{:n}".format(f_val), "\t", "{:n}".format(approximation))


if __name__ == "__main__":
    main()
