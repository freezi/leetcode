# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(cur, prev):
            if not cur:
                return prev
            else:
                temp = cur.next
                cur.next = prev
                return rev(temp, cur)
        
        return rev(head, None)