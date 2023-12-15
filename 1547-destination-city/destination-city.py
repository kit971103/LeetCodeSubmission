class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj = Counter()
        for start, end in paths:
            adj[start] -= 1
            adj[end] += 1
        return adj.most_common(1)[0][0]


            