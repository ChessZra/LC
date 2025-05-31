class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        money -= children

        n = money // 7
        remainder = money % 7

        if n == 0:
            return 0
        #print(n, remainder)
        if n > children:
            return children - 1
        elif n < children:
            if remainder == 3 and children - n == 1:
                return n - 1
            else:
                return n
        elif n == children:
            if remainder > 0:
                return children - 1
            else:
                return children
        
        """
        1 1 1
        8 8
        """