# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, tail):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                if cur == tail:
                    return
                cur = nxt
        current_group = 1
        dummy = ListNode(next=head)
        prev = dummy
        cur = dummy.next
        while cur:
            current_head = cur
            current_tail = None
            i = 0
            while cur and i < current_group:
                current_tail = cur
                cur = cur.next
                i += 1
            if i % 2 == 0:
                reverse(current_head, current_tail)
                current_head.next = cur
                prev.next = current_tail
                prev = current_head
            else:
                prev = current_tail
            current_group += 1
        return dummy.next