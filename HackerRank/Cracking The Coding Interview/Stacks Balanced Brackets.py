def is_matched(expression):
    pass
    dic1={'}':'{',')':'(',']':'['}
    arr=[]
    for c in expression:
        if c in dic1:
            if arr==None or len(arr)==0:
                return False
            c2=arr.pop(0)
            if not c2==dic1[c]:
                return False
        else:
            arr.insert(0,c)
    return True
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
