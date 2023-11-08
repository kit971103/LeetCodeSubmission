class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8: return False

        haveUpper = haveLower = haveDigit = haveSpecChar  = False
        SpecChar = "!@#$%^&*()-+"
        last_char = None
        
        for char in password:
            if char == last_char: return False
            if not haveUpper and char.isupper(): haveUpper = True
            if not haveLower and char.islower(): haveLower = True
            if not haveDigit and char.isnumeric(): haveDigit = True
            if not haveSpecChar and char in SpecChar: haveSpecChar = True
            last_char = char
        return haveUpper and haveLower and haveDigit and haveSpecChar
