class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        i=0
        j=0
        res=0
        unique=set(nums)
        unicount=len(unique)
        freq={}
        n=len(nums)
        while j<len(nums):
            
            if nums[j] in freq:
                freq[nums[j]]+=1
            else:
                freq[nums[j]]=1

            while len(freq)==unicount:
                res+=n-j

                freq[nums[i]] -= 1

                if freq[nums[i]]==0:
                    del freq[nums[i]]
        
                i+=1

            j+=1

        return res
            






