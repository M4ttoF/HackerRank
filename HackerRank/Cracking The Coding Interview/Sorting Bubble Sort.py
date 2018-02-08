n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubbleSort(arr,n):
    count=0
    while(True):
        flag=True
        for i in range(n-1):
            if arr[i+1]<arr[i]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=False
                count+=1
        if flag:
            break
    print('Array is sorted in {:d} swaps.'.format(count))
    print('First Element: {:d}'.format(arr[0]))
    print('Last Element: {:d}'.format(arr[-1]))
bubbleSort(a,n)