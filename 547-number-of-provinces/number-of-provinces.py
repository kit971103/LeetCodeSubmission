class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def visit(city):
            if visited[city]:
                return
            visited[city] = True
            for connectint_city, connected in enumerate(isConnected[city]):
                if connected:
                    visit(connectint_city)

        count = 0
        visited = [False] * len(isConnected)
        for city in range(len(isConnected)):
            if visited[city]:
                continue
            count+=1
            visit(city)
        return count




        