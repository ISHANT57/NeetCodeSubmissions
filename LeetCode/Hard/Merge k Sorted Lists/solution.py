# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        arr=[]

        for head in lists:
            while head:
                arr.append(head)
                head=head.next

        arr.sort(key=lambda x:x.val,reverse=True)

        head=None
        for num in arr:
            num.next=head
            head=num
        return head