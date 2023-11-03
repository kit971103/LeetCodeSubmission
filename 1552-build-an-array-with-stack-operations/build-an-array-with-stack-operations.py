class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        old = 0
        unit = ["Push", "Pop"]
        for n in target:
            if n > old + 1: res.extend( unit * (n-old-1))
            res.append("Push")
            old = n
        return res