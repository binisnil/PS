# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        passedNode = set()
        isCycled = False

        if head is None:
            return isCycled
        

        node = head
        while not isCycled:
            passedNode.add(node)
            if node.next is not None:
                isCycled = node.next in passedNode
                node = node.next
            else:
                break

        return isCycled