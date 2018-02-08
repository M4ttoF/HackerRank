import sys

def solve(arr, money):
    dic={}
    for i in range(len(arr)):
        if money-arr[i] in dic:
            print(str(dic[money-arr[i]])+' '+str(i+1))
            return None
        dic[arr[i]]=i+1
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
