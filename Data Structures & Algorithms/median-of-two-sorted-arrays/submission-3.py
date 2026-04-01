class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        for x in nums1:
            res.append(x)

        for x in nums2:
            res.append(x)

        res.sort()

        n = len(res)

        if n % 2 == 1:
            return res[n // 2]

        return (res[n // 2 - 1] + res[n // 2]) / 2