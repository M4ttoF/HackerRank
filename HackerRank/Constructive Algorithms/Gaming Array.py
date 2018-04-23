
import os
import sys


def gamingArray(arr):
    turn=1
    while(arr!=[]):
        arr=arr[:(arr.index(max(arr)))]
        turn*=-1
    if turn==1:
        return "ANDY"
    return "BOB"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
