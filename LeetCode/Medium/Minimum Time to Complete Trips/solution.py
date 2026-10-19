class Solution(object):


    def Ispossible(self,time,mid,totaltrips):

        trips=0

        for t in time:
            trips+=mid//t
        
        return trips>=totaltrips

    def minimumTime(self, time, totaltrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """


        

        left=1
        right=min(time)*totaltrips
        ans=-1

        while left<=right:

            mid=left+(right-left)//2

            if self.Ispossible(time,mid,totaltrips):
                ans=mid
                right=mid-1

            else:
                left=mid+1
        
        return ans