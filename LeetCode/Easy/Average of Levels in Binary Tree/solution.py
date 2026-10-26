# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self,node ):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res=[]

        if not node:
            return res

        queue=deque([node])

        while queue:
            avg=[]
            levelsize=len(queue)
            levelsum=0

            for i in range(len(queue)):
                node=queue.popleft()
                levelsum+=node.val
                avg.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)

            res.append(float(levelsum)/levelsize)
           

        return res
