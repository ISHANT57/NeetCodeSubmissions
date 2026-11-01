class Solution:
	def addBinary(self, s1, s2):
		# code here
		num1=int(s1,2)
		num2=int(s2,2)
		
		sumi=num1+num2
		
		return bin(sumi)[2:]
		