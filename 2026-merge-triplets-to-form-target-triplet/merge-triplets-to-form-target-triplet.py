class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False]*3
        for triplet in triplets:
            if not found[0] and target[0]==triplet[0] and target[1]>=triplet[1] and target[2]>=triplet[2]:
                found[0] = True
            if not found[1] and target[0]>=triplet[0] and target[1]==triplet[1] and target[2]>=triplet[2]:
                found[1] = True
            if not found[2] and target[0]>=triplet[0] and target[1]>=triplet[1] and target[2]==triplet[2]:
                found[2] = True
        return all(found)