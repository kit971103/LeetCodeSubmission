class Solution:
    def compressedString(self, word: str) -> str:
        result:list[str] = []
        count = 0
        rep = word[0]
        
        for c in word:
            if c == rep:
                if count == 9:
                    count = 1
                    result.append(f"9{rep}")
                else:
                    count += 1
            else:
                result.append(f"{count}{rep}")
                rep = c
                count = 1
        result.append(f"{count}{rep}")
        return "".join(result)
