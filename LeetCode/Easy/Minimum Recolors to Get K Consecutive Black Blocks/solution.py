class Solution(object):
    def minimumRecolors(self, nums, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
        i=0
        count=0
        best=k
        for j in range(len(nums)):

            if nums[j]=="W":
                count+=1

            if j-i+1==k:
                best=min(best,count)

                if nums[i]=="W":
                    count-=1
                i+=1
            
        
        return best