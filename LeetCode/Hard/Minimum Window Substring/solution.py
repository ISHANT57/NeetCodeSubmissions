class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(t)>len(s):
            return ""

        p=0

        dict1={}

        for ch in t:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1
        
        i=0
        j=0
        reqcount=len(t)
        minlen=float("inf")

        while j<len(s):
            ch=s[j]

            if ch not in dict1:
                dict1[ch]=0
            
            if dict1[ch]>0:
                reqcount-=1

            dict1[ch]-=1

            while reqcount==0:
                currlen=j-i+1

                if currlen<minlen:
                    minlen=currlen

                    start=i

                ch=s[i]
                dict1[ch]+=1

                if dict1[ch]>0:
                    reqcount+=1
                i+=1
            
            j+=1

        
        if minlen==float("inf"):
            return ""
        
        return s[start:start+minlen]

