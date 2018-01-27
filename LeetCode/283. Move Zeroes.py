class Solution(object):
    def moveZeroes(self, nums):
        z=0
        while 0 in nums:
            z+=1
            nums.remove(0)
        for i in range(0,z):
            nums.append(0)