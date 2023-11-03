class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        old = 0
        for i in range(len(target)):
            res.extend( ["Push", "Pop"] * (target[i]- (target[i-1] if i else 0) ))
            res.pop()
        return res