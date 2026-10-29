# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        ans=[]
        diff=0
        mini=float("inf")
        def inorder(node):
            if node is None:
                return []
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)

        for i in range(1,len(ans)):
            diff=ans[i]-ans[i-1]
            if diff<mini:
                mini=diff
        return mini
        