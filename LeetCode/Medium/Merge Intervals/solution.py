class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        start=intervals[0][0]
        end=intervals[0][1]

        n=len(intervals)
        ans=[]
        

        for i in range(1,n):
            s,e=intervals[i]

            if s<=end:
                end=max(end,e)
            
            else:
                ans.append((start,end))
                start=s
                end=e
        
        ans.append((start,end))
        return ans



        