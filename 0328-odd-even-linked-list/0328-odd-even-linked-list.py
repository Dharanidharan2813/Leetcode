# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        odd_increment = True
        even_increment = True
        
        while odd and even and (odd_increment or even_increment):
            if odd.next and odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            else:
                odd_increment = False
            
            if even.next and even.next.next:
                even.next = even.next.next
                even = even.next
            else:
                even_increment = False
        
        odd.next = even_head
        even.next = None
        
        return head