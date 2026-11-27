class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        ans=[]
        arr.sort()
        mini=float("inf")
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]

            if diff<mini:
                mini=diff
                ans=[]
            
            if diff==mini:

                ans.append((arr[i-1],arr[i]))
            
        return ans
        