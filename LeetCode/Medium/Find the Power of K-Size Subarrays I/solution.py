class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count=1
        ans=[]
        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]+1:

                count+=1
            else:
                count=1

            
            if i>=k-1:
                if count>=k:
                    ans.append(nums[i])
                
                else:
                    ans.append(-1)
        
        return ans
