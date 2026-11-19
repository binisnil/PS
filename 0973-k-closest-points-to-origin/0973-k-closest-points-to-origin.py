class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        result = sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]

        return result