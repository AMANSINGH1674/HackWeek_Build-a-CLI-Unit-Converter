import argparse


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    parser = argparse.ArgumentParser(
        description='CLI Unit Converter: Convert temperature between Celsius and Fahrenheit.'
    )
    parser.add_argument(
        'value',
        type=float,
        help='The temperature value to convert.'
    )
    parser.add_argument(
        '--to',
        choices=['celsius', 'fahrenheit'],
        required=True,
        help='The unit to convert to: "celsius" or "fahrenheit".'
    )

    args = parser.parse_args()

    if args.to == 'fahrenheit':
        result = celsius_to_fahrenheit(args.value)
        print(f"{args.value}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.value)
        print(f"{args.value}°F = {result:.2f}°C")


if __name__ == '__main__':
    main() 