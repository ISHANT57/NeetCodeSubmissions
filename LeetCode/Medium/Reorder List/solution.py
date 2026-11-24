# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        queue=deque()

        curr=head

        while curr:
            queue.append(curr)
            curr=curr.next

        
        while len(queue)>1:
            first=queue.popleft()
            last=queue.pop()

            first.next=last

            if queue:
                last.next=queue[0]
            else:
                last.next=None

        
        if queue:
            queue[0].next=None
        
        