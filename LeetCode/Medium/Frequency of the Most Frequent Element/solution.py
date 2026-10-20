class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        
        i=0
        j=0
        n=len(nums)
        currsum=0
        res=0
        
        while j<n:
            currsum+=nums[j]

            

            while nums[j] * (j - i + 1) - currsum > k:

                currsum-=nums[i]

                i+=1

            
            res=max(res,j-i+1)
            j+=1

        return res



