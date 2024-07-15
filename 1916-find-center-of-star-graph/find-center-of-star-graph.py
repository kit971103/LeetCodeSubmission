class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_a, edge_b = edges[0], edges[1]
        if (edge_a[0] == edge_b[0]) or (edge_a[0] == edge_b[1]):
            return edge_a[0]
        return edge_a[1]