import sys

def miniMaxSum(arr):
    arr=sorted(arr)
    #print arr
    low=long(0)
    high=long(0)
    for i in range(0,5):
        if i!= 4:
            low+=long(arr[i])
            #print low
        if i!=0:
            high+=long(arr[i])
            #print high
    print low,high

    
if __name__ == "__main__":
    arr = map(long, raw_input().strip().split(' '))
    miniMaxSum(arr)
