/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {

        ListNode slow=head;
        ListNode fast=head;

        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }

        ListNode rev = slow.next;
        slow.next=null;

        ListNode prev=null;

        while(rev!=null){
            ListNode nxt=rev.next;
            rev.next=prev;
            prev=rev;
            rev=nxt;

        }

        rev = prev;

        while(rev!=null){
            ListNode nxt1 = head.next;   
            ListNode nxt2 = rev.next;    

            head.next = rev;
            rev.next = nxt1;

            head = nxt1;
            rev = nxt2;
        }

        



        
        
    }
}
