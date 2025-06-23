import argparse
import sys


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit: F = (C × 9/5) + 32"""
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius: C = (F - 32) × 5/9"""
    return (f - 32) * 5/9


def main():
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit")
    
    temp_group = parser.add_mutually_exclusive_group(required=True)
    temp_group.add_argument('-c', '--celsius', type=float, help='Temperature in Celsius')
    temp_group.add_argument('-f', '--fahrenheit', type=float, help='Temperature in Fahrenheit')
    
    args = parser.parse_args()
    
    if args.celsius is not None:
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F = {result:.2f}°C")


if __name__ == "__main__":
    main()
