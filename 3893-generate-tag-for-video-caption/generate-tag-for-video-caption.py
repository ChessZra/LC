class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.split()
        if not caption:
            return '#'
        res = '#' + caption.pop(0).lower()

        for word in caption:
            c = ''
            for letter in word:
                if letter.isalpha():
                    c += letter
            
            res += c.capitalize()
        return res[:min(100, len(res))]