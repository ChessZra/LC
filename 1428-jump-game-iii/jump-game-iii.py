class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)

        visited = [False] * N
        def dfs(index):
            if index < 0 or index >= N:
                return False
            
            if arr[index] == 0:
                return True
            
            if visited[index]:
                return False
            
            visited[index] = True
            return dfs(index + arr[index]) or dfs(index - arr[index])
        return dfs(start)