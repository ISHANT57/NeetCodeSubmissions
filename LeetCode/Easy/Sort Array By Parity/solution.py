class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        even=[]
        odd=[]
        ans=[]

        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        
        ans.extend(even)
        ans.extend(odd)


        return ans        