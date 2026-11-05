class Solution:
    def searchMatrix(self, mat, x): 
    	# code here 
    	
    	row=len(mat)
    	cols=len(mat[0])
    	
    	
    	low=0
    	high=row*cols-1
    	
    	
    	while low<=high:
    	    
    	    
    	    mid=low+(high-low)//2
    	    
    	    r=mid//cols
    	    c=mid%cols
    	    
    	    if mat[r][c]==x:
    	        return True
    	       
    	    elif mat[r][c]<x:
    	        low=mid+1
    	        
    	    else:
    	        high=mid-1
        return False

