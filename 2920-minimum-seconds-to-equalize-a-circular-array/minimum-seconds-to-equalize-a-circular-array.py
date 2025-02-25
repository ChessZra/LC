class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        N = len(nums)
        mp = {}
        for i in range(N - 1, -1, -1):
            if nums[i] not in mp:
                mp[nums[i]] = i
            
        last_index = {}
        mx = {}
        for i in range(N):
            if nums[i] in last_index:
                mx[nums[i]] = max(mx.get(nums[i], 0), i - last_index[nums[i]])
            else:    
                if mp[nums[i]] > i:
                    mx[nums[i]] = max(mx.get(nums[i], 0), N - mp[nums[i]] + i)
            last_index[nums[i]] = i

        if not mx:
            return N // 2

        mn = min(mx.values())

        return mn // 2