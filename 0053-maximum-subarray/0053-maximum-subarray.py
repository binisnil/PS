class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        min_prefix = min(0, nums[0]) 
        result = nums[0]
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            result = max(result, prefix_sum[i] - min_prefix)
            min_prefix = min(min_prefix, prefix_sum[i])
        return result




