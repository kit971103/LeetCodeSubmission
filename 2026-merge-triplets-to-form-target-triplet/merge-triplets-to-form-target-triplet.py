class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False]*3
        x,y,z = target

        for a,b,c in triplets:
            if not found[0] and x==a and y>=b and z>=c:
                found[0] = True
            if not found[1] and x>=a and y==b and z>=c:
                found[1] = True
            if not found[2] and x>=a and y>=b and z==c:
                found[2] = True
        return all(found)