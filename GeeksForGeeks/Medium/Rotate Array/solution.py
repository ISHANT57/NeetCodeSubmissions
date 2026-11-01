class Solution:
    def rotateArr(self, arr, d):
        # code here
        
        n=len(arr)
        
        if n==0:
            return []
        
        d=d%n
        
        def reverse(arr,l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)
                
        
        