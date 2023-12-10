class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = [False] * len(isConnected)
        for city in range(len(isConnected)):
            if visited[city]:
                continue
            count +=1
            stack = deque([city])
            while stack:
                for _ in range(len(stack)):
                    city = stack.popleft()
                    if visited[city]:
                        continue
                    visited[city] = True
                    for i, x in enumerate(isConnected[city]):
                        if x: stack.append(i)
        return count




        