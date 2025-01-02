class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        N = len(people)
        f = collections.Counter()
        for i in range(N):
            f[i] = people[i][1] # person: count
        
        res = []
        seen = set()
        while True:
            found = None
            for i in range(N):
                if f[i] == 0 and i not in seen:
                    seen.add(i)
                    found = i
                    break

            for i in range(N):
                if people[found][0] >= people[i][0] and i not in seen:
                    f[i] -= 1
            
            res.append([people[found][0], people[found][1]])
            if len(seen) == N:
                break
                
        return res