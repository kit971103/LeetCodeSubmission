class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc_arr = [ n for n in itertools.accumulate(arr, func = operator.xor)]
        return [ (acc_arr[left-1] if left else 0)^acc_arr[right] for left, right in queries]


        