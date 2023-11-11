class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.nextNode = dict()
        self.n = n
        for i in range(n): 
            self.nextNode[i] = []
        for from_node, to_node, cost in edges:
            self.nextNode[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.nextNode[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        min_cost = [float("inf")] * self.n
        visited = [False] * self.n

        visited[node1] = True
        min_cost[node1] = 0
        for each, cost in self.nextNode[node1]:
            min_cost[each] = cost
        
        while not visited[node2]:
            alist = [(cost,i) for i, (cost, TF) in enumerate(zip(min_cost, visited)) if not TF]
            _, node = min(alist)
            visited[node] = True
            for each, cost in self.nextNode[node]:
                min_cost[each] = min(min_cost[each], min_cost[node] + cost)

        return min_cost[node2] if min_cost[node2] != float("inf") else -1
        

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
