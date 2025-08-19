class Solution:
    def clumsy(self, n: int) -> int:
        eval_string = ''
        steps = ['*', '//', '+', '-']
        current = 0
        for i in range(n, 0, -1):
            eval_string += str(i)
            if i > 1:
                eval_string += steps[current]
            current += 1
            current %= 4
        return eval(eval_string)