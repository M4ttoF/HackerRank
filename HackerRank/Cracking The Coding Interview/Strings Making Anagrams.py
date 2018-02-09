def number_needed(a, b):
    ans=0
    dic1={}
    dic2={}
    for c in a:
        if not c in dic1:
            dic1[c]=1
        else:
            dic1[c]+=1
    for c in b:
        if not c in dic2:
            dic2[c]=1
        else:
            dic2[c]+=1
    lets='qwertyuiopasdfghjklzxcvbnm'
    for c in lets:
        num1=0
        num2=0
        if c in dic1:
            num1=dic1[c]
        if c in dic2:
            num2=dic2[c]
        ans+=abs(num1-num2)
    return ans
a = input().strip()
b = input().strip()

print(number_needed(a, b))
