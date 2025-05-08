class SnapshotArray:

    def __init__(self, length: int):
        # snaps, current value
        self.arr = [[(-1, 0)] for _ in range(length)]
        self.snaps = 0
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snaps, val))

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        nums = self.arr[index]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m][0] <= snap_id:
                l = m
            else:
                r = m - 1
    
        return nums[l][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)