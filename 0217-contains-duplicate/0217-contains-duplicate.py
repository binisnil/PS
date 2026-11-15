from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numCounter = Counter(nums)
        mostCommon = numCounter.most_common(1)[0][1]
        if  mostCommon > 1 :
            return True
        else:
            return False