class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        step = len(arr)//4
        for i, n in enumerate(arr):
            if n == arr[i+step]:
                return n
        return None
        