# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        
        while (fast.next):
            if not fast.next.next: 
                return False
            elif fast.next.next == slow.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
            
            