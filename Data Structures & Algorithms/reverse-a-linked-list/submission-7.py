# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # have 2 trackers, 1 for current and prev
        # prev will be null, current will be head/start of the LinkedList
        # have current.next point to prev
        # prev goes to current
        # current goes to current.next
        # loop this until current == null
        # return prev as this will be the new head
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        