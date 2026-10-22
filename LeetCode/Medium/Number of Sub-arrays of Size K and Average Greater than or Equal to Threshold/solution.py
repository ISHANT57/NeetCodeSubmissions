class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        

        currsum=0
        count=0
        i=0
        j=0

        while j<len(arr):

            currsum+=arr[j]

            if (j-i+1)>k:
                currsum-=arr[i]
                i+=1

            if(j-i+1)==k:
                if currsum>=k*threshold:
                    count+=1
            j+=1

        
        return count