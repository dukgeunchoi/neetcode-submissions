# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()

        while list1 and list2:
            if list1.val >= list2.val:
                temp = list2.next
                list2.next = None
                curr.next = list2
                curr = curr.next
                list2 = temp
            else:
                temp = list1.next
                list1.next = None
                curr.next = list1
                curr = curr.next
                list1 = temp
        
        if not list1: curr.next = list2
        if not list2: curr.next = list1

        return head.next