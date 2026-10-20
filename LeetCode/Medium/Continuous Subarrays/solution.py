class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        j=0

        count=0
        freq={}
        n=len(nums)

        while j<n:

            freq[nums[j]]=freq.get(nums[j], 0) + 1

            while abs(max(freq)-min(freq))>2:
                freq[nums[i]]-=1

                if freq[nums[i]]==0:
                    del freq[nums[i]]
                i+=1

            count+=j-i+1

            j+=1

        return count

