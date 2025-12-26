from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1 = l1
        one = 0
        while l1 is not None or l2 is not None:
            val_l1 = 0
            val_l2 = 0

            if l1 is not None:
                val_l1 = l1.val

            if l2 is not None:
                val_l2 = l2.val

            val = val_l1 + val_l2 + one
            one = 0

            if val > 9:
                val = val % 10
                one = 1

            l1.val = val

            if l1.next is None and l2 is not None and l2.next is not None:
                l1.next = ListNode(0)
            elif one == 1 and l1.next is None:
                l1.next = ListNode(one)
                one = 0

            l1 = l1.next
            l2 = l2.next if l2 is not None and l2.next is not None else None

        return head_l1


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
#
# l1 = create_linked_list([0])
# l2 = create_linked_list([0])
# result = Solution().addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))

l1 = create_linked_list([2, 4, 9])
l2 = create_linked_list([5, 6, 4, 9])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))

l1 = create_linked_list([0])
l2 = create_linked_list([7, 3])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))
