class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1={}
        for s in strs:
            count=[0]*(26)

            for ch in s:
                count[ord(ch)-ord("a")]+=1

            key=str(count)

            if key not in dict1:
                dict1[key]=[]
            dict1[key].append(s)
        
        return list(dict1.values())
        