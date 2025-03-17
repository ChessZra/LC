class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # you can use a trie
        # or bruteforce
        N = len(nums)
        lookup = set(nums) # n is 16 -> not necessary

        for i in range(18):
            sbin = bin(i)[2:]
            sbin = (N - len(sbin)) * '0' + sbin
            
            if sbin not in lookup:
                return sbin
    
        return ""