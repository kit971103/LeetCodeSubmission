class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - int(round(purchaseAmount + 0.1, -1))