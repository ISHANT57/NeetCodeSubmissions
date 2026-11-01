class Solution:
    def getSecondLargest(self, arr):
        # code here
        # seen=set()
        
        # for i in arr:
        #     seen.add(i)
            
        # if len(seen)<2:
        #     return -1
        
        # first=max(seen)
        # seen.remove(first)
        # second=max(seen)
        
        # return second
        
        first=-1
        second=-1
        
        for i in arr:
            if i>first:
                first=i
        
        for i in arr:
            if i>second and i!=first:
                second=i
        
        return second
        
        
        
        
        
        
        