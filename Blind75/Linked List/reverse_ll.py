# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        # 1 -> 2 -> 3 

        """
        Concept: 
            We will use three pointers: prev, curr, and temp.
            - prev will point to the previous node (initially None).
            - curr will point to the current node we are processing (initially head).
            - temp will temporarily store the next node to process.

            Paperclip concept: you've 3 clips -> 1->2->3 - you need to now reverse them to 3->2->1. 

            Let's deal with 1 & prev node (Null) - let's store 2 somewhere (temp). Now, 1 should point to Null (prev). (curr.next -> prev, so 1->Null).
            Now, move prev to curr (prev = curr, so prev now points to 1). Move curr to temp (curr = temp, so curr now points to 2).

            Analogy: So, I need to store the next clip first (temp = curr.next), then point curr.next to prev
            In layman terms: point current clip to previous clip (1 -> 0), and before moving forward, make the current clip as previous one. 
            Now, go to the next clip (temp) and repeat the process until curr is None.
        """

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev