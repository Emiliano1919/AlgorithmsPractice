# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            newHead=self.reverseList(head.next) #Notice we always return the NewHead, we do not modify it
            ## Head.next.next instead of using prev because if not we are overwriting what we want to return
            head.next.next=head
        head.next=None #We have to break cycles

        return newHead