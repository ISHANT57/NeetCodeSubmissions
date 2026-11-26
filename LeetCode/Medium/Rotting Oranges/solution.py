class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n=len(grid)
        m=len(grid[0])
        time=0
        fresh=0
        queue=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                if grid[i][j]==1:
                    fresh+=1
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c,time=queue.popleft()

            for dx,dy in directions:
                x=r+dx
                y=c+dy

                if x<0 or x>=n or y<0 or y>=m or grid[x][y]==0:
                    continue
                if grid[x][y]==1:
                    grid[x][y]=2
                    fresh-=1
                    queue.append((x,y,time+1))
        
        if fresh>0:
            return -1
        
        return time


        