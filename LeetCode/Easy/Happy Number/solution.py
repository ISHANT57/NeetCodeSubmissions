class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        
        while n!=1:
            
            if n in seen:
                return False
            seen.add(n)
            
            sumi=0
            while n>0:
                digit=n%10
                sumi+=digit*digit
                n=n//10
            n=sumi
            
            
        return True
        