#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(" ".join([str(item) for item in arr[::-1]]))
