class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def unwrap(f):
            return lambda arg: f(*arg)
        res = 0
        boxTypes.sort(reverse = True, key = unwrap(lambda a,b: (b,a)) )
        for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
            boxesLoaded = min(numberOfBoxes, truckSize)
            res += boxesLoaded*numberOfUnitsPerBox
            truckSize -= boxesLoaded
            if truckSize == 0: break
        return res