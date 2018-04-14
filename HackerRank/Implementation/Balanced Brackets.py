import os
import sys


def is_matched(expression):
    stack=[]
    dic={']':'[',')':'(','}':'{'}
    for c in expression:
        if c not in dic:
            stack.append(c)
        elif len(stack)==0 or stack[-1] != dic[c]:
            return False
        else:
            stack.pop()
    if len(stack)==0:
        return True
    return False
        

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

