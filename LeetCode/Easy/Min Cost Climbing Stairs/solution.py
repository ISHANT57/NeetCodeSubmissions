class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp=[0]*(n+1)

        dp[0]=0
        dp[1]=0


        for i in range(2,n+1):
            one=dp[i-1]+cost[i-1]
            two=dp[i-2]+cost[i-2]

            dp[i]=min(one,two)

        return dp[n]

        



        