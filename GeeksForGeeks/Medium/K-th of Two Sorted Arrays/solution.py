class Solution:
    def kthElement(self, a, b, k):
        # code here
        m=len(a)
        n=len(b)
        
        a[:m+n]=sorted(a[:m]+b)
        
        
        return a[k-1]
                