# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def findBadVersion(left: int, right: int) :
            if left > right:
                return
            
            mid = (left + right) // 2

            if isBadVersion(mid) and isBadVersion(mid - 1):
                return findBadVersion(left, mid-1)
            elif isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid):
                return findBadVersion(mid+1, right)
            
        return findBadVersion(1, n)