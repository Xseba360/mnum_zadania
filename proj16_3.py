import math
from typing import Callable


def rectangle_method(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    current_value = 0.0
    h = (b - a) / n

    for k in range(n + 1):
        current_value += f(a + k * h)

    current_value *= h

    return current_value


def simpson_method(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    s1 = 0.0
    s2 = 0.0
    h = (b - a) / n

    for k in range(1, n + 1):
        x = a + k * h
        s2 += f(x - (h / 2.0))
        if k < n:
            s1 += f(x)

    current_value = (h / 6.0) * (f(a) + f(b) + 2.0 * s1 + 4.0 * s2)

    return current_value


def main():
    func: Callable[[float], float] = lambda x: 2 * (1 / (1 + x ** 2) + 1 / (2 * x) - 3 * x ** 3)

    F: Callable[[float], float] = lambda x: 2 * (math.atan(x) + 0.5 * math.log(abs(x)) - 3 / 4 * x ** 4)

    a = 1
    b = 5

    n = 200

    # Obliczanie wartości dokładnej całki
    exact_integral = F(b) - F(a)

    # Obliczanie całki metodą Simpsona
    simpson_result = simpson_method(func, a, b, n)

    # Obliczanie całki metodą prostokątów
    rectangle_result = rectangle_method(func, a, b, n)

    error_simpson = abs(simpson_result - exact_integral)
    error_rectangle = abs(rectangle_result - exact_integral)

    print(F(a))
    print(F(b))
    print(f"Exact Integral: {'{:.15f}'.format(exact_integral)}")
    print(f"Integral (Simpson): {'{:.15f}'.format(simpson_result)}")
    print(f"Error (Simpson): {'{:.15f}'.format(error_simpson)}")
    print(f"Integral (rectangles): {'{:.15f}'.format(rectangle_result)}")
    print(f"Error (rectangles): {'{:.15f}'.format(error_rectangle)}")


if __name__ == "__main__":
    main()
