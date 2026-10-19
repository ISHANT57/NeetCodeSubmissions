class Solution(object):

    def canEat(self, piles,mid,h):

        hour=0

        for i in piles:
            hour+=i//mid

            if i%mid!=0:
                hour+=1
        
        return hour<=h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """


        left=1
        right=max(piles)
        ans=-1

        while left<=right:
            mid=left+(right-left)//2

            if self.canEat(piles,mid,h):
                ans=mid
                right=mid-1
            
            else:
                left=mid+1
        return ans
        