class Solution:
    def kthMissing(self, arr, k):
        
        # count=0
        # x=1
        # temp=[]
       
        # while count<k:
        #     if x not in arr:
                
        #         arr.append(x)
        #         temp.append(x)
        #         count+=1
                
        #     x+=1
        
        
        # return temp[k-1]
        # s=set(arr)
        # curr=0
        
        # while count<k:
        #     curr+=1
            
        #     if curr not in s:
        #         count+=1
        
        # return curr
        n=len(arr)
        for i in range(n):
            
            if arr[i]>i+k:
                return i+k
        
        return n+k
                
            
            