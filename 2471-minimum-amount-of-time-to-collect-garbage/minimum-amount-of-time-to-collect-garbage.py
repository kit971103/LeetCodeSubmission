class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_seen_P = last_seen_G = last_seen_M = res = 0
        total_travled = list(n for n in itertools.accumulate(travel, initial = 0))
        for i, recycle_box in enumerate(garbage):
            res += len(recycle_box)
            if "P" in recycle_box: last_seen_P = i
            if "G" in recycle_box: last_seen_G = i
            if "M" in recycle_box: last_seen_M = i
        return res + total_travled[last_seen_P] + total_travled[last_seen_G] + total_travled[last_seen_M]
            
            





        