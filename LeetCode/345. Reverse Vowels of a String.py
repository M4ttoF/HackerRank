class Solution:
    def reverseVowels(self, s):
        
        vowels={'a':True,'e':True,'i':True,'o':True,'u':True}
        c=s.lower()
        pos=[]
        for i in range(len(s)):
            if c[i] in vowels:
                pos.append(i)
        arr=list(s)
        ans=''
        for i in range(len(pos)//2):
            arr[pos[i]],arr[pos[(i*-1)-1]]=arr[pos[(i*-1)-1]],arr[pos[i]]
        for p in arr:
            ans+=p;
            
        return ans
      