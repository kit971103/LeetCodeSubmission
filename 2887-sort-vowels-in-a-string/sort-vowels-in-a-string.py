class Solution:
    def sortVowels(self, s: str) -> str:
        isVOWELS ="aeiouAEIOU"
        vowels = [ c for c in s if c in isVOWELS]
        if not vowels: return s

        vowels.sort(reverse = True)
        t = [ c if c not in isVOWELS else vowels.pop() for c in s]

        return "".join(t)