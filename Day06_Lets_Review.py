# Enter your code here. Read input from STDIN. Print output to STDOUT
def even_odd(testcase):
    eve = [testcase[s] for s in range(0, len(testcase), 2)]
    odd = [testcase[s] for s in range(1, len(testcase), 2)]
    print("".join(eve), "".join(odd))

T = int(input())

test = [input() for i in range(T)]

for i in range(T):
    even_odd(test[i])
    
