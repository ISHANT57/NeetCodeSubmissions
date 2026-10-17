class Solution:
    def findTarget(self, arr, target):
        # code here
        low=0
        high=len(arr)-1
        
     
        
        while low<=high:
            
            mid=low+(high-low)//2
            
            if arr[mid] == target:
                
                return mid
            
            if mid>low and arr[mid-1]==target:
                return mid-1
                
            if mid<high and arr[mid+1]==target:
                return mid+1
                
            
            if arr[mid]<target:
                low=mid+2
            
            else:
                high=mid-2
                
        
        return -1
            
            
            