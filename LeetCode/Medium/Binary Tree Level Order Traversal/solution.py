# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):

        res=[]
        if root is None:
            return res

        queue=deque()
        queue.append(root)
        

        while len(queue)>0:
            curr=[]

            for i in range(len(queue)):

                root=queue.popleft()

                curr.append(root.val)

                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)

            res.append(curr)
    
        return res
        