import sys

def diagonalDifference(a):
    # Complete this function
    fSum=0
    lSum=0
    for i in range(0,len(a)):
        fSum+=a[i][i]
        lSum+=a[i][abs(abs(i-len(a))-1)%len(a)]
    return abs(fSum-lSum)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
