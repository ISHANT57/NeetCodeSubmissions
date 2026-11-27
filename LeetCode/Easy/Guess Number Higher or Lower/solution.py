# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n

        while low<=high:
            mid=(low+high)//2
            pick=guess(mid)

            if pick==0:
                return mid
            
            elif 0<pick:
                low=mid+1
            
            else:
                high=mid-1
                
        