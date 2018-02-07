import sys


n=int(input())
arr=input()
arr=arr.split()
for i in range(n-1,-1,-1):
    print(arr[i],end=' ')
