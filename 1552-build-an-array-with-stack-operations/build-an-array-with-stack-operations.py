class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        old = 0
        for n in target:
            if n > old + 1: res.extend( ["Push", "Pop"] * (n-old-1))
            res.append("Push")
            old = n
        return res