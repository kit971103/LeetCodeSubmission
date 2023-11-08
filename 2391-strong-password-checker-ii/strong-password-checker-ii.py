class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8: return False

        haveUpper = haveLower = haveDigit = haveSpecChar  = False
        Lower = "qwertyuiopasdfghjklzxcvbnm"
        Upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        Digit = "1234567890"
        SpecChar = "!@#$%^&*()-+"
        last_char = None
        
        for char in password:
            if char == last_char: return False
            elif not haveUpper and char in Upper: haveUpper = True
            elif not haveLower and char in Lower: haveLower = True
            elif not haveDigit and char in Digit: haveDigit = True
            elif not haveSpecChar and char in SpecChar: haveSpecChar = True
            last_char = char
        return haveUpper and haveLower and haveDigit and haveSpecChar
