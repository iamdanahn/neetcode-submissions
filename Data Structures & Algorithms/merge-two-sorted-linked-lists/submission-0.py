# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one at each LL
        # compare node values at each pointer
        # send smaller one to new LL
        # repeat until one side of the LL is empty
        # add the entire remaining LL of the other side
        # return head of new LL
        p1 = list1
        p2 = list2
        head = ListNode()
        cur = head

        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next

        if p1 == None:
            cur.next = p2
        else:
            cur.next = p1

        return head.next