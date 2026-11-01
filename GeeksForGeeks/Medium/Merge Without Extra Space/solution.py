class Solution:
    def mergeArrays(self, a, b):
        # code here
        m=len(a)
        n=len(b)
        
        # a[:m+n]=sorted(a[:m]+b)
        
        c=sorted(a+b)
        a[:]=c[:len(a)]
        b[:]=c[len(a):]
        
        
        