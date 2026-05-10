# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next=list1 #This way we do not need to create new ListNode
                list1=list1.next
            else:
                node.next= list2
                list2= list2.next
            node=node.next #This is to move to the next
        node.next= list1 or list2 #If one is empty the other one is the whole thing
        return dummy.next #The first node is a dummy the dummy.next is head