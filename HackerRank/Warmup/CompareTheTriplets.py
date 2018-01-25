import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a=[a0,a1,a2]
    b=[b0,b1,b2]
    Ali=0
    Bob=0
    for i in range(0,3):
        if a[i]>b[i]:
            Ali+=1
        elif b[i]>a[i]:
            Bob+=1
    return Ali, Bob
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
