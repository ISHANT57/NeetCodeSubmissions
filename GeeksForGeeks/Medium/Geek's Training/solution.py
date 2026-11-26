class Solution:
    def maximumPoints(self, mat):
        # code here
        a=b=c=0
        
        # print(mat)
        
        for u,v,w in mat:
            na=u+max(b,c)
            nb=v+max(a,c)
            nc=w+max(a,b)
            
            a, b, c = na, nb, nc
        
        return max(a,b,c)