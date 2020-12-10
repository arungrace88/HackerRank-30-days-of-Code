#!/bin/python3

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max = -1000

    for row in range(0, 4):
        for col in range(0, 4):
            sum_list = []
            sum_list.append(arr[row][col])
            sum_list.append(arr[row][col + 1])
            sum_list.append(arr[row][col + 2])
            sum_list.append(arr[row + 1][col + 1])
            sum_list.append(arr[row + 2][col])
            sum_list.append(arr[row + 2][col + 1])
            sum_list.append(arr[row + 2][col + 2])
            #
            if sum(sum_list) > max: max = sum(sum_list)


    print(max)
