class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money: return -1
        if money > 8 * children: return children - 1
        money-=children
        ans = money //7
        if (ans == children - 1) and money%7 == 3: return ans - 1
        return ans
        