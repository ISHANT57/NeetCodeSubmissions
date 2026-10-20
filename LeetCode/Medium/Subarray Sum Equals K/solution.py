class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefixsum=0
        count=0
        freq={0:1}

        for num in nums:
            prefixsum+=num

            need=prefixsum-k
            if (need) in freq:
                count+=freq[need]
            
            if prefixsum in freq:
                freq[prefixsum]+=1
            
            else:
                freq[prefixsum]=1
        return count