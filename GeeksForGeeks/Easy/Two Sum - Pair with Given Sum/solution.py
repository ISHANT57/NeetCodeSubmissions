class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()
		l=0
		r=len(arr)-1
		
		while l<r:
		    total=arr[l]+arr[r]
		    
		    if total==target:
		        return True
	        elif total<target:
	            l+=1
            else:
                r-=1
        return False