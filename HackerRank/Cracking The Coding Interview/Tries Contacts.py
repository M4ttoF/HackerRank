dic={}
lets='qwertyuiopasdfghjklzxcvbnm'
for c in lets:
    dic[c]=[]

def addTo(d, name):
    d[name[0]].append(name)

def findSeq(d, seq):
    num=0
    for i in d[seq[0]]:
        if i.startswith(seq):
            num+=1
    print(num)
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op=='add':
        addTo(dic,contact)
    elif op=='find':
        findSeq(dic,contact)
