import sys
import bisect

n = int(input().strip())
a = []
a_i = 0
size=0

def findMed(arr, s):
    
    if s%2 ==1:
        if s==1:
            return float(arr[0])
        return float(arr[s//2])
    else:
        return (float(arr[s//2-1])+float(arr[(s//2)]))/2

for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(a,a_t)
    size+=1
    print(findMed(a,size))
    
