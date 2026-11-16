class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.heap=[]

        for num in stones:
            heapq.heappush(self.heap,-num)
        
        while len(self.heap)>1:
            a=-heapq.heappop(self.heap)
            b=-heapq.heappop(self.heap)
            diff=a-b

            if diff>0:
                heapq.heappush(self.heap,-diff)

        if self.heap:
            return -self.heap[0]
        return 0
            
