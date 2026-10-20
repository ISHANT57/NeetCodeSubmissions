class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        i=0
        j=0
        
        n=len(nums)
        currsum=0
        maxsum=0
        freq={}
        
        while j<n:

            currsum+=nums[j]

            if nums[j] in freq:
                freq[nums[j]]+=1
            else:
                freq[nums[j]]=1

            if j-i+1>k:
                currsum-=nums[i]
                freq[nums[i]] -=1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]

                i += 1
            
            if j-i+1==k and len(freq)==k:
                maxsum=max(maxsum, currsum)

            j+=1
        return maxsum

