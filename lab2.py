import csv
from decimal import Decimal, getcontext
from collections import OrderedDict


def interpolation_method(data: OrderedDict[Decimal, Decimal], x_value: Decimal) -> Decimal:
    interpolated_value: Decimal = Decimal('0')
    for x_argument, y_value in data.items():
        term = y_value
        for other_x_argument in data.keys():
            if other_x_argument != x_argument:
                term *= (x_value - other_x_argument) / (x_argument - other_x_argument)
        interpolated_value += term
    return interpolated_value


def main() -> None:
    data: OrderedDict[int, int] = OrderedDict({
        -2: -34,
        0: 0,
        1: -1,
        3: -9,
    })

    converted_data: OrderedDict[Decimal, Decimal] = OrderedDict(
        (Decimal(str(k)), Decimal(str(v))) for k, v in data.items()
    )

    start: Decimal = min(converted_data.keys())
    end: Decimal = max(converted_data.keys())

    step: Decimal = Decimal('0.2')

    getcontext().prec = 10

    result: OrderedDict[Decimal, Decimal] = OrderedDict()

    for i in range(int((end - start) / step) + 1):
        x: Decimal = start + Decimal(i) * step
        y: Decimal = interpolation_method(converted_data, x)
        result[x] = y
        print('{:n},\t{:f}'.format(x, y))

    result_as_string: OrderedDict[str, str] = OrderedDict(
        ("{:n}".format(k), "{:f}".format(v)) for k, v in result.items()
    )

    with open("lab2_result.csv", "w") as outfile:
        csvwriter = csv.writer(outfile, quoting=csv.QUOTE_ALL, delimiter=',', quotechar='"', lineterminator='\n')
        csvwriter.writerows(result_as_string.items())


if __name__ == '__main__':
    main()
