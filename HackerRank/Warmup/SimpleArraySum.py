import sys

def simpleArraySum(n, ar):
    # Complete this function
    k=0
    for num in ar:
        k+=num
    return k
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)