from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        haveOdd = False
        result = 0
        for n in counter.values():
            result += n // 2 * 2
            if (n % 2 == 1) and not haveOdd:
                result += 1
                haveOdd = True
        
        return result



        