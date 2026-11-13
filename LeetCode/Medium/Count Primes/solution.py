class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isprime=[True]*n
        
        if n<2:
            return 0
        isprime[0]=isprime[1]=False
        
        for i in range(2,int(n**0.5)+1):
            if isprime:
                for j in range(i*i,n,i):
                    isprime[j]=False
                    
        return sum(isprime)