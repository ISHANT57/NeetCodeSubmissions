class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict1={}

        for i in range(len(numbers)):
            rem=target-numbers[i]

            if rem in dict1:
                return [dict1[rem],i+1]

            dict1[numbers[i]]=i+1
        