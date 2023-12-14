class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node, target, val):
            if visited[node]:
                return -1
            visited[node] = True
            result = -1
            for other, multiplier in mul_table[node]:
                if other == target:
                    return val*multiplier
                x = dfs(other, target, val*multiplier)
                if x > 0:
                    return x
            visited[node] = False
            return -1


        mul_table = defaultdict(list)
        for (n, d), val in zip(equations, values):
            mul_table[n].append((d, val))
            mul_table[d].append((n, 1/val))

        # res = [ (dfs(n, d, 1) if not(n in mul_table and d in mul_table) else -1.0) for n,d in queries]
        res = []
        for n, d in queries:
            if not(n in mul_table and d in mul_table):
                res.append(-1.0)
            else:
                visited = { c : False for c in mul_table.keys() } # reset visited
                res.append(dfs(n, d, 1))
        return res

        