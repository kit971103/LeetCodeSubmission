class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc_arr = [ n for n in itertools.accumulate(arr, func = operator.xor, initial = 0)]
        return [ acc_arr[left]^acc_arr[right+1] for left, right in queries]


        