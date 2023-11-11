class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.adj_list = [[] for _ in range(n)]

        for from_node, to_node, cost in edges:
            self.adj_list[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.adj_list[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        
        min_cost = [ float("inf") ] * len(self.adj_list)
        min_cost[node1] = 0
        heap = [(0, node1)]

        while heap:
            precost, node = heappop(heap)
            if node == node2: return precost
            for neighbor, cost in self.adj_list[node]:
                new_cost = precost + cost
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heappush(heap, (new_cost, neighbor))
        return -1
        

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
