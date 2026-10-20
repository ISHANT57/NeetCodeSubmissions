class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        

        n=len(s)
        m=len(p)

        if m>n:
            return []

        q=0

        freq={}
        freq2={}
        while q<m:
            freq[p[q]]=freq.get(p[q],0)+1

            q+=1
        
        i=0
        j=0
        res=[]

        while j<n:

            freq2[s[j]]=freq2.get(s[j],0)+1


            if (j-i+1)==m:
                if freq==freq2:
                    res.append(i)

                freq2[s[i]] -= 1

                if freq2[s[i]]==0:
                    del freq2[s[i]]

                i+=1
            
            j+=1
        return res

            


        
