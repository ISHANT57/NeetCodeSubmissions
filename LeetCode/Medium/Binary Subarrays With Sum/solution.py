class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
        freq={0:1}

        currsum=0
        count=0

        for num in nums:
            currsum+=num

            need=currsum-goal

            if need in freq:
                count+=freq[need]

            
            if currsum in freq:
                freq[currsum]+=1
            else:
                freq[currsum]=1
        return count

