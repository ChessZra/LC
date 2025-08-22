class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        N = len(friends)
        INF = 10 ** 20
        pq = [(id, 0)]
        visited = [False] * N
        dist = [INF] * N
        dist[id] = 0
        while pq:
            cur, dst = heappop(pq)
            if visited[cur]:
                continue
            visited[cur] = True
            for friend in friends[cur]:
                dist[friend] = min(dist[friend], dst + 1)
                heappush(pq, (friend, dst + 1))
        chars = collections.Counter()
        for person, value in enumerate(dist):
            if value == level:
                for vid in watchedVideos[person]:
                    chars[vid] += 1
        res = sorted(chars.items(), key=lambda x:(x[1], x[0]))
        return [x[0] for x in res]
            
