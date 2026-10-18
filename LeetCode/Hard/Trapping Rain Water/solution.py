class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        leftmax=rightmax=water=0
        left=0
        right=len(height)-1

        while left<right:

            if height[left]<=height[right]:

                leftmax=max(leftmax,height[left])
                water+=leftmax-height[left]
                left+=1
            
            else:

                rightmax=max(rightmax,height[right])
                water+=rightmax-height[right]
                right-=1

        
        return water



            