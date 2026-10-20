class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        i=0
        j=1
        n=len(colors)
        k=3
        N=n+k-1

        

        res= colors+colors[:k - 1]

        result=0

        while j<N:
            if res[j]==res[j-1]:
                i=j
                j+=1
                continue
            
            
            if (j-i+1)==k:
                result+=1
                i+=1
                
            
            j+=1

        return result
