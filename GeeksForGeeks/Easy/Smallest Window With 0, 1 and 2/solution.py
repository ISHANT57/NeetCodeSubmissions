class Solution:
    def smallestSubstring(self, s):
        # code here
        
        i=0
        j=0
        
        res=float('inf')
        
        n=len(s)
        freq={}
        
        while j<n:
            
            if s[j] in freq:
                freq[s[j]]+=1
            else:
                freq[s[j]]=1
                
            
            while len(freq)==3:
                
                res=min(res,j-i+1)
                
                freq[s[i]]-=1
                
                if freq[s[i]] == 0:
                    
                    del freq[s[i]]
                    
                i+=1
            j+=1
        
        if res==float("inf"):
            return -1
        return res
                
                