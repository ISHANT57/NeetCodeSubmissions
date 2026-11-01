class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        citations.reverse()
        count=0
        
        
        
        for i in range(len(citations)):
            if citations[i]>=i+1:
                count+=1
            else:
                break
        
        return count