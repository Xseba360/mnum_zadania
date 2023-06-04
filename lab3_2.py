import math
from collections import OrderedDict
from typing import Tuple


def calculate_coefficients(data: OrderedDict[float, float]) -> Tuple[
    Tuple[float, float],
    Tuple[float, float],
    Tuple[float, float, float]
]:
    num_data_points = len(data)
    log_x = [math.log(x_val) for x_val in data.keys()]
    log_f = [math.log(f_val) for f_val in data.values()]

    sum_log_x_squared = sum(log_x_val ** 2 for log_x_val in log_x)
    sum_log_x = sum(log_x)
    sum_log_f_times_log_x = sum(log_f_val * log_x_val for log_f_val, log_x_val in zip(log_f, log_x))
    sum_log_f = sum(log_f)

    determinant_g = sum_log_x_squared * num_data_points - sum_log_x ** 2
    determinant_a = sum_log_f_times_log_x * num_data_points - sum_log_x * sum_log_f
    determinant_b = sum_log_x_squared * sum_log_f - sum_log_f_times_log_x * sum_log_x

    coefficient_a1 = determinant_a / determinant_g
    coefficient_b1 = determinant_b / determinant_g

    final_a = math.exp(coefficient_b1)
    final_b = coefficient_a1

    return (final_a, final_b), (coefficient_a1, coefficient_b1), (determinant_g, determinant_a, determinant_b)


def main() -> None:
    data: OrderedDict[float, float] = OrderedDict({
        1.0: 1.8,
        3.0: 8.5,
        4.0: 9.5,
        6.0: 20.0,
    })

    (
        final_a,
        final_b
    ), (
        coefficient_a1,
        coefficient_b1
    ), (
        determinant_g,
        determinant_a,
        determinant_b
    ) = calculate_coefficients(data)

    print("General determinant: ", determinant_g)
    print()
    print("Determinant a: ", determinant_a)
    print("Determinant b: ", determinant_b)
    print()
    print("Coefficient a1: ", coefficient_a1)
    print("Coefficient b1: ", coefficient_b1)
    print()
    print("Final coefficient a: ", final_a)
    print("Final coefficient b: ", final_b)
    print()
    print("Approximation:")
    print("x", "\t", "f", "\t", "a * x^b")

    for x_val, f_val in data.items():
        approximation = final_a * x_val ** final_b
        print("{:n}".format(x_val), "\t", "{:n}".format(f_val), "\t", "{:n}".format(approximation))


if __name__ == "__main__":
    main()
