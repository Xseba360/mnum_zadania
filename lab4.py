import random
from typing import Callable


def trapezoidal_method(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    current_value = 0.0
    h = (b - a) / n

    for k in range(1, n + 1):
        current_value += f(a + k * h)

    current_value = (current_value + ((f(a) + f(b)) / 2.0)) * h

    return current_value


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


def monte_carlo_method(f: Callable[[float], float], xp: float, xk: float, n: int) -> float:
    current_value = 0.0
    h = (xk - xp)

    for _ in range(n):
        current_value += f(xp + (random.random()) * h)

    return h * (current_value / n)


def main():
    func: Callable[[float], float] = lambda x: 1 / (1 + x ** 2)

    # Interval [a, b]
    a = -4.0
    b = 4.0

    # Number of subdivisions
    n = [10, 100, 2000, 20000]

    for i in range(len(n)):
        rectangles = rectangle_method(func, a, b, n[i])
        print(f"Integral value (rectangle method): {rectangles} for n={n[i]}")

    for i in range(len(n)):
        trapezoids = trapezoidal_method(func, a, b, n[i])
        print(f"Integral value (trapezoidal method): {trapezoids} for n={n[i]}")

    for i in range(len(n)):
        simpsons = simpson_method(func, a, b, n[i])
        print(f"Integral value (Simpson's method): {simpsons} for n={n[i]}")

    for i in range(len(n)):
        monte_carlos = monte_carlo_method(func, a, b, n[i])
        print(f"Integral value (Monte Carlo method): {monte_carlos} for n={n[i]}")


if __name__ == "__main__":
    main()
