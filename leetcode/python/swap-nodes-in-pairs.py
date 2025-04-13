# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_node = ListNode(0, head)
        prev = fake_node
        current = head
        while current and current.next:
            nextPair = current.next.next
            second = current.next

            second.next = current
            current.next = nextPair
            prev.next = second
            prev = current
            current = nextPair

        return fake_node.next

if __name__ == '__main__':
    data = [
            [1,2,3,4], 
            #[1,2,3],
        ]
    
    sol = Solution()
    for arr in data:
        first = ListNode(arr[0])
        prev = first
        
        for i in range(len(arr)):
            if i == 0:
                continue
            current = ListNode(arr[i])
            prev.next = current
            prev = current
        
        cur = first

        # while cur is not None:
        #     print(cur.val, cur.next)
        #     cur = cur.next

        answer = sol.swapPairs(first)

        while not answer is None:
            print(answer.val, answer.next)
            answer = answer.next       
        