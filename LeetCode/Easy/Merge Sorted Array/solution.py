class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # ans=[]

        # for i in range(m):
        #     ans.append(nums1[i])
        # # print(ans)
        # for i in range(n):
        #     ans.append(nums2[i])
        # print(ans)


        # nums1=ans

        nums1[:m+n]=sorted(nums1[:m]+nums2)
        return nums1
        
       