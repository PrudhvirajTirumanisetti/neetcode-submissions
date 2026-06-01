# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head 

        #find the middle
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

        secondList = slow.next
        dummy = slow.next = None

        #reverse the second linked list
        while secondList:
            temp = secondList.next
            secondList.next = dummy
            dummy = secondList
            secondList = temp 
        
        #merge two linked lists

        first, second = head, dummy

        while second:
            temp1, temp2 = first.next, second. next
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2    