class Solution:
	def preGreaterEle(self, arr):
		# code here
		
		stack=[]
		
		ans=[-1]*(len(arr))
		
		for i in range(len(arr)-1,-1,-1):
		    while stack and arr[i]>arr[stack[-1]]:
		        j=stack.pop()
		        ans[j]=arr[i]
	        
	        stack.append(i)
        
        return ans