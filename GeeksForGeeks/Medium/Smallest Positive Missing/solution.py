class Solution:
    def missingNumber(self, arr):
        # code here
        
        seen=set(arr)
        num=1
        
        while num in seen:
            num+=1
        
        return num
            
                