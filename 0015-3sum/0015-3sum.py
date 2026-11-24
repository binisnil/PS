class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:   # x 중복 건너뛰기
                continue

            l, r = i + 1, n - 1
            
            while l < r:
                # 합이 x보다 크면 -> 오른쪽 포인터를 왼쪽으로 이동
                if nums[l] + nums[r] > -nums[i]:
                    r = r - 1
                # 합이 x보다 작으면 -> 왼쪽 포인터를 오른쪽으로 이동
                elif nums[l] + nums[r] < -nums[i]:
                    l = l + 1
                # 합이 x면 -> num[i], num[l], num[r]을 res에 append
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # [while문] 왼쪽 포인터가 같은 값이면 계속 건너뛰기 (중복 제거)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # [while문] 오른쪽 포인터가 같은 값이면 계속 건너뛰기 (중복 제거)
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res