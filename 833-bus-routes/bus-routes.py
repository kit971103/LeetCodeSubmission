class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target: return 0

        routes_adj_list = []
        
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            routes_adj_list.append(set())
            for stop in routes[i]:
                if len(routes_adj_list[i]) >= i: break
                for j in range(i):
                    if stop in routes[j]: 
                        routes_adj_list[i].add(j)
                        routes_adj_list[j].add(i)

        length = 1
        source = set( i for i, route in enumerate(routes) if source in route)
        queue = []
        for i, route in enumerate(routes):
            if target not in route: continue
            if i in source: return length
            queue.append(i)

        seen = set(queue)

        while queue:
            new_queue = []
            length += 1
            for route in queue:
                for neighbour in routes_adj_list[route]:
                    if neighbour not in seen: 
                        if neighbour in source: return length
                        new_queue.append(neighbour)
                        seen.add(neighbour)
            queue = new_queue.copy()
        return -1









        