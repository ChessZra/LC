class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        res = 0
        def can(bit_position, current_array):
            if bit_position == -1:
                return
            nonlocal res 
            new_array = []
            bad = False
            for lst in current_array:
                arr = []
                for num in lst:
                    if num & 2 ** bit_position == 0:
                        arr.append(num)
                if arr:
                    new_array.append(arr)
                else: # this part has to count to the answer
                    bad = True
                    break
            if not bad:
                can(bit_position - 1, new_array)
            else:  
                res += 2 ** bit_position
                can(bit_position - 1, current_array)
        can(18, grid)
        return res