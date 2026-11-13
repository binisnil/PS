from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major = len(nums) // 2
        count = Counter(nums)

        for i in count:
            if count[i] > major:
                return int(i)
        