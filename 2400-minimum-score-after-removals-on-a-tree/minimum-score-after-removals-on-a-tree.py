from itertools import combinations
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        subtree_xor: list[int] = [0] * len(nums)
        descendants: list[set[int]] = [set() for _ in range(len(nums))]
        adjacency_list: list[set[int]] = [set() for _ in range(len(nums))]
        result = None

        for i, j in edges:
            adjacency_list[i].add(j)
            adjacency_list[j].add(i)

        def dfs(node: int, parent: int):
            t_xor = nums[node]
            t_descendant = {node}
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                t_xor ^= subtree_xor[neighbor]
                t_descendant |= descendants[neighbor]
            # cache it
            subtree_xor[node] = t_xor
            descendants[node] = t_descendant

        dfs(0, -1)  # start DFS from node 0
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                if i in descendants[j]:
                    scores = (
                        subtree_xor[i] ^ subtree_xor[j],
                        subtree_xor[i],
                        subtree_xor[0] ^ subtree_xor[j],
                    )
                elif j in descendants[i]:
                    scores = (
                        subtree_xor[i] ^ subtree_xor[j],
                        subtree_xor[j],
                        subtree_xor[0] ^ subtree_xor[i],
                    )
                else:
                    scores = (
                        subtree_xor[i],
                        subtree_xor[j],
                        subtree_xor[0] ^ subtree_xor[j] ^ subtree_xor[i],
                    )
                score = max(scores) - min(scores)
                if result is None or score < result:
                    result = score

        return result