class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        N = len(s)

        def solve(left, right):
            res = 0
            stk = [] 
            for i in range(left, right + 1):
                if s[i] == '(':
                    stk.append(i)
                else:
                    last = stk.pop()
                
                    if not stk:
                        if last + 1 == i:
                            res += 1
                        else:
                            res += 2 * solve(last + 1, i - 1)
            return res
        
        return solve(0, N - 1)