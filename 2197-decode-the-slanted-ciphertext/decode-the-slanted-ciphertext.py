class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = len(encodedText)
        RL = N // rows
        res = ''
        last_letter = 0
        for i in range(RL):
            idx = i
            while idx < N:
                res += encodedText[idx]
                if encodedText[idx] != ' ':
                    last_letter = len(res)
                idx += (RL + 1)
        return res[:last_letter]