import sys


arr = []
tot= -92233720368547758
for i in range(6):
    row=input()
    arr.append(row.split())
for y in range(4):
    for x in range(4):
        z=0
        for p in range(3):
            z+=int(arr[y][x+p])
        z+=int(arr[y+1][x+1])
        for p in range(3):
            z+=int(arr[y+2][x+p])
        if z>tot:
            tot=z
print(tot)