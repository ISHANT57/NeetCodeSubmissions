class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        q=deque()

        ans=[]

        j=0
        while j<len(nums):
            while q and nums[q[-1]]<=nums[j]:
                q.pop()
            
            q.append(j)

            if q[0]<=j-k:
                q.popleft()
            
            if j>=k-1:
                ans.append(nums[q[0]])
            
            j+=1

        return ans