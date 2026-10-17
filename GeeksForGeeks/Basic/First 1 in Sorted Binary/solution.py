class Solution:
    def firstIndex(self, arr):
        # code here
        
        low=0
        high=len(arr)-1
        ans=-1
        while low<=high:
            
            mid=low+(high-low)//2
            
            if arr[mid]==1:
                ans=mid
                high=mid-1
                
            elif arr[mid]<1:
                low=mid+1
            else:
                high=mid-1
                
        return ans
                

