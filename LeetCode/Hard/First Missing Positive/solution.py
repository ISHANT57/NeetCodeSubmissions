class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
      
        check=[]
        for i in nums:
            if i>0:
                check.append(i)
        check.sort()

        for i in range(len(check)):
            if check[i]>i+1:
                return i+1
        
        return len(check)+1
        
        
