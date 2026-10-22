class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        i=0
        j=0

        zeros=0

        ans=0

        for j in range(len(nums)):

            if nums[j]==0:
                zeros+=1

            
            while zeros>k:
                if nums[i]==0:
                    zeros-=1

                i+=1

            ans=max(ans,j-i+1)
        
            

        return ans
