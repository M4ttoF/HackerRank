import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    count=0
    low=-1
    for a in ar:
        if a>low:
            low=a
            count=1
        elif a==low:
            count+=1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
