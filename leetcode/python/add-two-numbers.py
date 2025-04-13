from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curL1 = l1
        curL2 = l2
        add = 0

        while curL1 is not None:
            l1Val = curL1.val
            l2Val = curL2.val
            sum = l1Val + l2Val + add
            add = 0
            if sum > 9:
                add = sum // 10
                sum = sum % 10
            curL1.val = sum    
            curL1 = curL1.next
            curL2 = curL2.next

        if add != 0:
            curL1.next = ListNode(add)

        return l1  
    
    def reverseList(self, l: Optional[ListNode]):
        cur = l
        revesedL = []
        while cur is not None:
            revesedL.insert(0, cur)
            cur = cur.next

        
        return


def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# l1 = create_linked_list([2, 4, 3])
# l2 = create_linked_list([5, 6, 4])
# result = Solution().addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))

# l1 = create_linked_list([0])
# l2 = create_linked_list([0])
# result = Solution().addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))
