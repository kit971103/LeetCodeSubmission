class Solution:
    def secondHighest(self, s: str) -> int:
        try:
            return sorted(list(set(map(int, filter(lambda c: c.isnumeric(), s)))))[-2]
        except IndexError:
            return -1
        