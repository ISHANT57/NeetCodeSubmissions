# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if root is None:
            return []

        res=[]
        queue=deque()
        queue.append(root)

        while queue:
            size=len(queue)
            curr=[]

            for i in range(size):
                node=queue.popleft()
                curr.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            res.append(curr[-1])

        return res       