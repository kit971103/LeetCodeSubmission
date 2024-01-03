class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        floorDevs = []
        totalBeam= 0
        for floor in bank:
            floorDev = floor.count("1")
            if floorDev != 0: 
                floorDevs.append(floorDev)
        for i in range(len(floorDevs)-1):
            totalBeam += floorDevs[i]*floorDevs[i+1]      
        return totalBeam