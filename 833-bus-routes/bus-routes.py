class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        bus_in_stop = defaultdict(list)
        
        for bus, route in enumerate(routes):
            for stop in route:
                bus_in_stop[stop].append(bus)
        
        queue = bus_in_stop[source]
        length = 1
        visited_stop = {source}
        visited_bus = set(queue)

        while queue:
            next_queue = []
            for bus in queue:
                for stop in routes[bus]:
                    if stop in visited_stop: continue
                    if stop == target: return length
                    visited_stop.add(stop)
                    for next_bus in bus_in_stop[stop]:
                        if next_bus not in visited_bus:
                            visited_bus.add(next_bus)
                            next_queue.append(next_bus)
            queue = next_queue.copy()
            length+=1
        return -1
                    
                    





        

            








        