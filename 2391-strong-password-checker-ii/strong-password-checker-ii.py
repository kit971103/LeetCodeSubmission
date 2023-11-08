class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8: return False

        for char in password:
            if char.islower(): break
        else: return False

        for char in password:
            if char.isupper(): break
        else: return False

        for char in password:
            if char.isnumeric(): break
        else: return False
        
        SpecChar = "!@#$%^&*()-+"
        for char in password:
            if char in SpecChar: break
        else: return False

        last_char = None
        for char in password:
            if char == last_char: return False
            last_char = char
        return True
