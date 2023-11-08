class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = math.floor(math.sqrt(area))
        for x in range(i, 0, -1):
            if area%x == 0: break
        return [area//x, x]
        