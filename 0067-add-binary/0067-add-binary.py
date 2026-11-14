class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_binary = '0b' + a
        b_binary = '0b' + b

        result = bin(int(a_binary, 2) + int(b_binary, 2))

        return result[2:]

        
