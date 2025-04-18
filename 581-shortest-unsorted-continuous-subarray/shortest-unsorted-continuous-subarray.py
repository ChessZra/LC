class Element:
    def __init__(self, index, element):
        self.idx = index
        self.num = element

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        mx = nums[0]
        stk = [Element(0, nums[0])]
        typeshi = float('inf')
        res = 0
        for i in range(1, N):
            changed = None
            while stk and stk[-1].num > nums[i]:
                res = max(res, i - stk[-1].idx + 1)
                changed = stk[-1].idx
                stk.pop()
            
            if changed is not None:
                typeshi = min(typeshi, changed)
                stk.append(Element(changed, nums[i]))
            else:
                stk.append(Element(i, nums[i]))

            mx = max(mx, nums[i])
            if mx > nums[i]:
                res = max(res, i - typeshi + 1)
        return res