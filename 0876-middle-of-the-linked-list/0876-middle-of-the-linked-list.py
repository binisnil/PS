# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        cnt = head
        result = head
        while cnt:
            count += 1
            cnt = cnt.next

        middle = count // 2

        for _ in range(middle):
            result = result.next
        return result