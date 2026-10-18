class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        positive=[] 
        negative=[]

        ans=[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)

            
        n=len(positive)
    
        for i in range(n):
            ans.append((positive[i]))
            ans.append((negative[i]))

        return ans

       
        