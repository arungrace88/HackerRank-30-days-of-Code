# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if __name__ == '__main__':
    n = int(input())
    phone = {}

    for i in range(n):
        cont = input().split()
        phone[cont[0]] = cont[1]

    entries = sys.stdin.readlines()
    for i in entries:
        name = i.strip()
        if name in phone:
            print(name + '=' + str(phone[name]))
        else:
            print('Not found')
