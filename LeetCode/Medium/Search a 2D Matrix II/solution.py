class Solution(object):
    def searchMatrix(self, matrix, target):
        
        n=len(matrix)
        m=len(matrix[0])

        r=0
        c=m-1

        while r<n and c>=0:
            if matrix[r][c]==target:
                return True
            
            elif matrix[r][c]<target:
                r+=1
            
            else:
                c-=1

        
        return False

 


        