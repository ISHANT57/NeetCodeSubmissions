class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        queue=deque()

        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        

        time=0
        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        while queue:

            for i in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in dir:

                    nr=r+dr
                    nc=c+dc


                    if nr<0 or nr>=n or nc<0 or nc>=m:
                        continue

                    if grid[nr][nc]!=1:
                        continue

                    
                    grid[nr][nc]=2
                    fresh-=1

                    queue.append((nr,nc))

            
            if len(queue)>0:
                time+=1

        if fresh>0:
            return -1

        return time

            



        