class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr=[]
        res=[]

        nums.sort()
        def backtrack(start):
            res.append(curr[:])


            for i in range(start,len(nums)):
                if i>start and  nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        
        return res
