from sortedcontainers import SortedList
class ExamRoom:
    """
      0 1 2 3 4 5 6 7 8 9
      ^   ^   ^         ^  
    """
    def __init__(self, n: int):
        self.n = n
        self.sorted_list = SortedList()

    def seat(self) -> int:

        if len(self.sorted_list) == 0:
            self.sorted_list.add(0)
            return 0

        mx_dist = 0
        res = 0
        prev = None
        # Seat in between seats
        for cur in self.sorted_list:
            if prev is None:
                prev = cur
                continue

            dist = cur - prev
            half = dist // 2

            if half > mx_dist:
                mx_dist = half
                res = prev + half
            prev = cur

        # Seat at seat 0?
        if self.sorted_list[0] >= mx_dist:
            mx_dist = self.sorted_list[0]
            res = 0
        
        # Seat at seat n - 1?
        if (self.n - 1 - self.sorted_list[len(self.sorted_list) - 1]) > mx_dist:
            res = self.n - 1
        
        self.sorted_list.add(res)
        return res

    def leave(self, p: int) -> None:
        self.sorted_list.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)