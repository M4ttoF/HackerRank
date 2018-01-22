import sys

def aVeryBigSum(n, ar):
    # Complete this function
    num=0
    for a in ar:
        num+=a
    return num

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
