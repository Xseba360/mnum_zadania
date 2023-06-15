from collections import OrderedDict
from typing import Tuple


def calculate_A_B_C_D(data: OrderedDict[float, float]) -> Tuple[float, float, float, float]:
    A: float = sum(x ** 2 for x in data.keys())
    B: float = sum(data.keys())
    C: float = sum(x * fx for x, fx in data.items())
    D: float = sum(fx for fx in data.values())
    return A, B, C, D


def calculate_W_a_b(n: int, A: float, B: float, C: float, D: float) -> Tuple[float, float, float]:
    W: float = A * n - B ** 2
    a: float = (C * n - B * D) / W
    b: float = (A * D - C * B) / W
    return W, a, b


def main() -> None:
    t_R: OrderedDict[float, float] = OrderedDict({
        25: 109.4,
        30: 110.1,
        35: 112.0,
        40: 114.7,
        45: 116.0,
        50: 118.1,
        55: 119.5,
        60: 121.8,
        65: 123.1,
        70: 124.9,
        75: 127.6,
        80: 129.4,
        85: 130.6,
        90: 131.9,
        95: 134.1,
    })

    A, B, C, D = calculate_A_B_C_D(t_R)
    n = len(t_R)  # 15
    W, a, b = calculate_W_a_b(n, A, B, C, D)
    R0 = b
    alpha = a / R0

    print(f"A = {A:.1f} B = {B:.1f} C = {C:.1f} D = {D:.1f} W = {W:.1f}")
    print(f"a = {a:.5f} b = {b:.5f}")
    print(f"R_0 = {R0:.5f} alpha = {alpha:.5f}\n")

    print("t,R(x),a*x+b")
    for x, fx in t_R.items():
        print(f"{x:.0f},{fx:.1f},{(a * x + b):.5f}")


if __name__ == "__main__":
    main()
