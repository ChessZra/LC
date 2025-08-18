class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        N = len(arr)
        current = N
        for index in range(N - 1, -1, -1):
            if current == arr[index]:
                current -= 1
            else:
                where = arr.index(current)
                arr = arr[:where+1][::-1] + arr[where+1:]
                arr = arr[:index+1][::-1] + arr[index+1:]
                res.append(where + 1)
                res.append(index + 1)
                current -= 1
        return res