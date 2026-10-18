class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        left=0
        right=len(nums)-1
        ans=0
        mod=10**9+7

        while left<=right:

            if nums[left]+nums[right]<=target:
                ans = (ans + 2**(right-left))%mod
                left+=1
            else:
                right-=1
        
        return ans
        