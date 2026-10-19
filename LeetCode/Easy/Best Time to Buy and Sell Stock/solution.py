class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mini=float("inf")
        maxprofit=0

        for price in prices:
            mini=min(mini,price)
            maxprofit=max(maxprofit,price-mini)

        return maxprofit
        