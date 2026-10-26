# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]


        """  

        if root is None:
            return []
        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            level=len(queue)
            curr=[]
            for i in range(level):
                node=queue.popleft()
                curr.append(node.val)
                # print(curr)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(curr)
            # print(res)
        
        return res[::-1]

