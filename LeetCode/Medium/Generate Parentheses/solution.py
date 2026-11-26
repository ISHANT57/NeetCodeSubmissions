class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def dfs(s,left,right):
            if len(s)==2*n:
                ans.append(s)
                return 

            if left<n:

                dfs(s+"(",left+1,right)
            if right<left:

                dfs(s+")",left,right+1)

        dfs("",0,0)
        return ans