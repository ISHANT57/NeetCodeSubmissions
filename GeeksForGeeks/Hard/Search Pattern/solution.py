class Solution:
    def search(self, pat, txt):
        # code here
        
        ans=[]
        i=0
        
        while True:
            idx=txt.find(pat,i)
            
            if idx==-1:
                break
            ans.append(idx)
            i=idx+1
        
        return ans
            