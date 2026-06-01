# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() # default val 0, next none
        dummy.next = head # connect to the LL 
        ahead = behind = dummy # start two pointers, ahead is n postions ahead of behind

        for _ in range(n+1): # inclusive of n
            ahead = ahead.next # move n places
        
        #go until ahead is at the end of the linked list 
        while ahead: 
            ahead = ahead.next 
            behind = behind.next

        #now behind is exactly on n-1 postion. 
        behind.next = behind.next.next 

        return dummy.next