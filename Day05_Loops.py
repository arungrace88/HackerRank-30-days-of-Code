#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    for i in range(1, 11):
        mult = i*n
        print(" ".join([str(n), "x", str(i), "=", str(mult)]))

