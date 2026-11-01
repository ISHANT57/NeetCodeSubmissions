class Solution:
	def pushZerosToEnd(self, arr: list[int]) -> None:
    	# code here
    	start=0
    	
    	for i in range(len(arr)):
    	    if arr[i]!=0:
    	        arr[start],arr[i]=arr[i],arr[start]
    	        start+=1
    	