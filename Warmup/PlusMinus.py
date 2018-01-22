import sys

def plusMinus(arr):
    # Complete this function
    counter=[0,0,0]
    
    for a in arr:
        if a > 0:
            counter[0]+=1
        elif a < 0:
            counter[1]+=1
        else:
            counter[2]+=1
    for c in counter:
        avg=c/len(arr)
        print('%1.6f' % avg)
    
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
