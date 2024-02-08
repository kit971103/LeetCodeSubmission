class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(key*freq for key, freq in Counter(s).most_common())

