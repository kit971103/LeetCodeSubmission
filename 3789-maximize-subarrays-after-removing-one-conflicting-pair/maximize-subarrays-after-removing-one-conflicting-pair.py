class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [ [] for _ in range(n+1)]
        for pair in conflictingPairs:
            right[max(pair)].append(min(pair))

        left = [0, 0]
        total = 0
        bouns = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                left = max(left, [left[0], l], [l, left[0]])

            total += r - left[0]
            bouns[left[0]] += left[0] - left[1]

        return total +max(bouns)
