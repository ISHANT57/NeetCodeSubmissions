class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans=[[]]

        for x in nums:
            for i in range(len(ans)):
                ans.append(ans[i]+[x])
        
        return ans