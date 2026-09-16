# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ):
        currOne = list1
        currTwo = list2

        output = sortedList = ListNode()

        while currOne and currTwo:
            if currOne.val > currTwo.val:
                sortedList.next = currTwo
                sortedList = sortedList.next
                currTwo = currTwo.next
                continue

            if currOne.val <= currTwo.val:
                sortedList.next = currOne
                sortedList = sortedList.next
                currOne = currOne.next
                continue

            sortedList.next = currOne
            sortedList = sortedList.next
            currOne = currOne.next

        sortedList.next = currOne or currTwo

        return output.next