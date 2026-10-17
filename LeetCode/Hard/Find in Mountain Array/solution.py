# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, arr):


        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        

        n=arr.length()
        peak=-1
        low=0
        high=n-1

        while low<high:
            mid=low+(high-low)//2

            if arr.get(mid)<arr.get(mid+1):
                low=mid+1
            else:
                high=mid

        
        peak=low


        low=0
        high=peak

        while low<=high:
            mid=low+(high-low)//2
            

            if arr.get(mid)==target:
                return mid

            elif arr.get(mid)<target:
                low=mid+1

            else:
                high=mid-1

        

        low=peak+1
        high=n-1

        while low<=high:
            mid=low+(high-low)//2

            if arr.get(mid)==target:
                return mid
            
            elif arr.get(mid)>target:
                low=mid+1
            else:
                high=mid-1

        return -1
