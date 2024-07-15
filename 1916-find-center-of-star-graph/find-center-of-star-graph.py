class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e1 = edges[0][0]
        return e1 if (e1 == edges[1][0]) or (e1 == edges[1][1]) else edges[0][1]
