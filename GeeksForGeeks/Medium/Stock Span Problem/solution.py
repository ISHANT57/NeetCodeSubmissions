class Solution:
    def calculateSpan(self, prices):
        # code here
        stack=[]
        ans=[]
        for price in prices:
            span=1

            while stack and stack[-1][0]<=price:
                span+=stack[-1][1]
                stack.pop()
            stack.append((price,span))
            ans.append(span)
        return ans
        