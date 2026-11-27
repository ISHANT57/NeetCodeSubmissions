class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        

        n=len(matrix)
        m=len(matrix[0])

        for i in range(1,n):
            for j in range(m):
                left=max(0,j-1)
                right=min(m,j+2)
            
                matrix[i][j]+=min(matrix[i-1][left:right])
        
        return min(matrix[-1])