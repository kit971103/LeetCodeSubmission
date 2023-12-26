class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def is_updatable(update, traget, index):
            for i, a, b in zip(itertools.count(), update, traget):
                if (i!=index and a > b) or (i==index and a != b):
                    return False
            return True


        
        found = [False]*3

        for triplet in triplets:
            if not found[0] and is_updatable(triplet, target , 0):
                found[0] = True
            if not found[1] and is_updatable(triplet, target , 1):
                found[1] = True
            if not found[2] and is_updatable(triplet, target , 2):
                found[2] = True
        
        return all(found)
        