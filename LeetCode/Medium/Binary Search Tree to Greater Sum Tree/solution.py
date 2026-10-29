# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        total = [0]
        def revinorder(node):
           
            if node is None:
                return 

            revinorder(node.right)
            total[0]+=node.val
            node.val=total[0]

            revinorder(node.left)
        
        revinorder(root)
        return root