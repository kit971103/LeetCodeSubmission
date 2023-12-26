class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def is_updatable(update, traget, index):
            for i, a, b in zip(itertools.count(), update, traget):
                if (i!=index and a > b) or (i==index and a != b):
                    return False
            return True

        found = [False]*3

        for triplet in triplets:
            for i in range(3):
                if not found[i] and is_updatable(triplet, target , i):
                    found[i] = True

        return all(found)
        