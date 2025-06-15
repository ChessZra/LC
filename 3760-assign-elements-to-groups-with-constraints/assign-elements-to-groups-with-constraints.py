class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        visited = [-1] * (max(groups) + 1)

        for index, num in enumerate(elements):
            
            if num >= len(visited):
                continue

            if visited[num] != -1:
                continue

            for i in range(num, len(visited), num):
                if visited[i] == -1:
                    visited[i] = index

        #print(visited)
        ans = []
        for g in groups:
            ans.append(visited[g])

        return ans


        """
        3 6 9
        2 4 6 8 10 12 14
        """