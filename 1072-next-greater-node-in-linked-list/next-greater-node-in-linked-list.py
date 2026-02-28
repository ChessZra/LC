# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        index = 0
        stk = []
        while head != None:
            res.append(0)
            while stk and head.val > stk[-1][0]:
                res[stk.pop()[1]] = head.val
            stk.append((head.val, index))
            index += 1
            head = head.next
        return res