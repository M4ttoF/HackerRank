
import sys
def getWays(n, c):
    # Complete this function
    c=sorted(c)
    j=n-c[0]
    global combs,found
    combs=[]
    found=[]
    def getComb(at,goal,com):
        if(at==goal):
            com=sorted(com)
            if(com not in combs[goal-1]):
     #           print(goal,com,at)
                combs[goal-1].append(com)
        elif(at<goal):
            if(combs[goal-at-1]!=[]):
                for q in combs[goal-at-1]:
                    getComb(goal,goal,com+q)
            else:
                for k in c:
                    if k<= goal:
                        getComb(at+k,goal,sorted(com+[k]))
                    else:
                        break;

    #adding the combinations
    #find which numbers add up to i
    for i in range(n):
        combs.append([])

        getComb(at=0,goal=i+1,com=[],)
    print(len(combs[n-1]))
getWays(10,[2,3,4,5])
'''    
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
'''