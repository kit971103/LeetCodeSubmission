class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_seen_P = last_seen_G = last_seen_M = res = 0
        for i, recycle_box in enumerate(garbage):
            res += len(recycle_box)
            if "P" in recycle_box: last_seen_P = i
            if "G" in recycle_box: last_seen_G = i
            if "M" in recycle_box: last_seen_M = i
        acc = 0
        for i, time in enumerate(travel, 1):
            acc+=time
            if i == last_seen_P: res += acc
            if i == last_seen_G: res += acc
            if i == last_seen_M: res += acc
            if i >= last_seen_P and i >= last_seen_G and i >= last_seen_M: break
            
        return res 
            
            





        