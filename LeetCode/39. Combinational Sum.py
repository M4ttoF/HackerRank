class Solution(object):
    def combinationSum(self, candidates, target):
        global sol, cans
        sol=[]
        cans=sorted(candidates)
        print(cans)
        def find(num,sofar):
            if num==0:
                sofar=sorted(sofar)
                if sofar not in sol:
                    sol.append(sofar)
                return
            for c in cans:
                if c>num:
                    break
                find(num-c,sofar+[c])
        find(target,[])
                    
        return sol