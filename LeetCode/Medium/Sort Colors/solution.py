class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.


        """

        # nums.sort()

        one=two=zero=0

        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1

        
        i=0

        for j in range(zero):
            nums[i]=0
            i+=1
        for j in range(one):
            nums[i]=1
            i+=1
        for j in range(two):
            nums[i]=2
            i+=1

        return nums

        