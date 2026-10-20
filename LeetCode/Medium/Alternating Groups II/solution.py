class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        
        i=0
        j=1
        n=len(colors)

        N=n+k-1

        if k == 1:

            
            return len(colors)

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
