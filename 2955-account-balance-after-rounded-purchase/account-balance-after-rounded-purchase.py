class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - purchaseAmount//10 * 10 - (10 if purchaseAmount%10 > 4 else 0)