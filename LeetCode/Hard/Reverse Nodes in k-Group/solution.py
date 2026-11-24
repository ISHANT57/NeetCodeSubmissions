# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        stack=[]
        dummy=curr=ListNode(0)

        while head:
            stack.append(head)
            head=head.next

            if len(stack)==k:
                while stack:
                    curr.next=stack.pop()
                    curr=curr.next
        
        if stack:
            curr.next=stack[0]
        else:
            curr.next=None
        
        return dummy.next
        