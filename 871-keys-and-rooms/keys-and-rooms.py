class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(keys):
            for key in keys:
                if visited[key]: continue
                visited[key] = True
                dfs(rooms[key])
        
        visited = [False] * len(rooms)
        visited[0] = True
        dfs(rooms[0])
        return all(visited)



        