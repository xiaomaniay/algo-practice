class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # newHead = pre = ListNode(0)
        # pre.next = head
        # while head:
        #     i = 0
        #     temp = head
        #     while i <= n and temp:
        #         i += 1
        #         temp = temp.next
        #     if i == n and not temp:
        #         pre.next = head.next
        #         break
        #     pre = head
        #     head = head.next
        # return newHead.next
        newHead = slow = fast = ListNode(0)
        newHead.next = head

        for i in range(n + 1):
            fast = fast.next
            if not fast and i < n:
                return head
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return newHead.next


if __name__ == "__main__":
    test = Solution()
    testList = ListNode(2)
    testList2 = ListNode(1)
    testList2.next = testList
    print(testList2)
    print(test.removeNthFromEnd(testList2, 2))
