#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    lArgv = len(argv) - 1
    if lArgv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(exit(1))
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print(f"{a} + {b} =", add(a, b))
        elif argv[2] == "-":
            print(f"{a} - {b} =", sub(a, b))
        elif argv[2] == "*":
            print(f"{a} * {b} =", mul(a, b))
        elif argv[2] == "/":
            print(f"{a} / {b} =", div(a, b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print(exit(1))
