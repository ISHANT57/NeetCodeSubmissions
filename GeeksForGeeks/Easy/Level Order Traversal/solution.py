''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def levelOrder(self, root):
        # code here
        
        res=[]
        queue=deque()
        
        queue.append(root)
        
        while queue:
            size=len(queue)
            curr=[]
            for i in range(size):
                node=queue.popleft()
                
                curr.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            
            res.extend(curr)
        
        
        return res
                
                