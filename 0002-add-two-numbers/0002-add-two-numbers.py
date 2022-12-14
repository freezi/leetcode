# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.val += l2.val
        remainder = l1.val // 10
        l1.val = l1.val % 10
        
        s = l1
        
        while (l1.next or l2.next):
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()
            
            l1 = l1.next
            l2 = l2.next
            
            l1.val += l2.val + remainder
            remainder = l1.val // 10
            l1.val = l1.val % 10
            
        if remainder:
            l1.next = ListNode(1)
        
        return s