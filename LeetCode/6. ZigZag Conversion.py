class Solution(object):
    def convert(self, s, numRows):
        
        sol=[]
        for i in range(0,numRows):
            sol.append("")
        pos=0
        flag=False
        if(numRows==1):
            return s
        for c in s:
            if(pos==numRows):
                flag=True
                pos-=2
            if(flag==False):
                sol[pos]+=c
                pos+=1
            else:
                if(pos<2):
                    flag=False
                sol[pos]+=c
                pos-=1
        ans=""
        for x in sol:
            ans+=x

        return ans
            
        