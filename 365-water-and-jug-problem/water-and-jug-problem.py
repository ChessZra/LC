class Solution:
    def canMeasureWater(self, cap_x: int, cap_y: int, target: int) -> bool:
        
        def pour(x, y, cap_x, cap_y):
            dist_to_full = cap_y - y
            if dist_to_full <= x:
                return (x - dist_to_full, cap_y)
            else:
                return (0, y + x)

        visited = set()
        def solve(x, y):
  
            if (x + y) == target:
                return 1
            
            if x > cap_x or y > cap_y or (x, y) in visited:
                return 0

            visited.add((x, y))

            best = 0
            # fill either jug completely
            best = max(best, solve(cap_x, y), solve(x, cap_y))
            # empty the thing
            best = max(best, solve(0, y), solve(x, 0))
            # pour x
            new_x, new_y = pour(x, y, cap_x, cap_y)
            best = max(best, solve(new_x, new_y))
            # pour y
            new_x, new_y = pour(y, x, cap_y, cap_x)
            best = max(best, solve(new_x, new_y))

            return best

        return bool(solve(0, 0))