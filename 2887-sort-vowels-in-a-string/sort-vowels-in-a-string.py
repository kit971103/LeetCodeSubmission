class Solution:
    def sortVowels(self, s: str) -> str:
        isVOWELS ="aeiouAEIOU"
        vowels = [ c for c in s if c in isVOWELS]
        if not vowels: return s

        vowels.sort(reverse = True)
        t = []

        for c in s:
            if c not in isVOWELS: t.append(c)
            else: t.append(vowels.pop())

        return "".join(t)