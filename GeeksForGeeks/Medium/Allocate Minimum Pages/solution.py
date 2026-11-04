class Solution:
    
    def allocatepages(self,arr,mid,k):
        
        pages=0
        stud=1
        for page in arr:
            
            if page+pages<=mid:
                pages+=page
            
            else:
                stud+=1
                pages=page
            
            
        
        
        return stud<=k
        
    def findPages(self, arr, k):
        # code here
        low=max(arr)
        high=sum(arr)
        
        if k>len(arr):
            return -1
      
        
        while low<high:
            
            mid=low+(high-low)//2
            
            if self.allocatepages(arr,mid,k):
                
                high=mid
            
            else:
                low=mid+1
                
        
        return low
