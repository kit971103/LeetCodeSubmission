class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        old = 0
        for n in target:
            res.extend( ["Push", "Pop"] * (n-old))
            res.pop()
            old = n
        return res