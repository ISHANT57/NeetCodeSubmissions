class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i=0
        ans=[]
        while i<len(word1) or i<len(word2):
            if i <len(word1):
                ans.append(word1[i])
            if i<len(word2):
                ans.append(word2[i])

            i+=1
        return "".join(ans)

        # ans=""

        # ans=word1+word2
        # n=len(ans)
        # ans=list(ans)
        # slow=0
        # fast=1
        # res=[]
        # for i in range(n):
        #     res.append(ans[slow])
        #     res.append(ans[fast])
        #     slow+=2
        #     fast+=2
        
        # return "".join(res)




        