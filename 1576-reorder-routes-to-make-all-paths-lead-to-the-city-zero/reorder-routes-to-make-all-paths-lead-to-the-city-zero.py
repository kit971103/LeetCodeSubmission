class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        to_city = [ [] for _ in range(n)]
        from_city = [ [] for _ in range(n)]
        for a, b in connections:
            to_city[b].append(a)
            from_city[a].append(b)
        
        # to_city = [ [start for start, end in connections if end == city] for city in range(len(connections)+1)]
        # from_city = [ [end for start, end in connections if start == city] for city in range(len(connections)+1)]

        count = 0
        stack = deque([0])
        visited = [False] * n
        visited[0] = True
        while stack:
            i = stack.popleft()
            for endcity in from_city[i]:
                if not visited[endcity]:
                    count +=1
                    visited[endcity] = True
                    stack.append(endcity)
            for startcity in to_city[i]:
                if not visited[startcity]:
                    visited[startcity] = True
                    stack.append(startcity)
        return count

            
            

