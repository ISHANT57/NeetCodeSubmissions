class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]

        n=len(s)
        res=""

        for i in range(n):
            if not stack or stack[-1]!=s[i]:
                stack.append(s[i])
            else:
                stack.pop()
        while stack:
            res+=stack.pop()

        return "".join(res[::-1])
        