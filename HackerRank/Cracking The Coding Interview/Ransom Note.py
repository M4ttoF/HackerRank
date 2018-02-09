def ransom_note(magazine, ransom):
    if len(magazine)<len(ransom):
        return False
    dic1={}
    for w in magazine:
        if not w in dic1:
            dic1[w]=1
        else:
            dic1[w]+=1
    for w in ransom:
        if not w in dic1:
            return False
        elif dic1[w]==0:
            return False
        else:
            dic1[w]-=1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
