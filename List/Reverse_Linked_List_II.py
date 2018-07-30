class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):

        dumHead = pre = ListNode(0)
        pre.next = head
        revLength = n - m

        while m > 1 and head:
            pre = head
            head = head.next
            m -= 1

        while revLength > 0 and head:
            temp = head.next
            head.next = temp.next
            temp.next = pre.next
            pre.next = temp
            revLength -= 1

        return dumHead.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    reslt = Solution().reverseBetween(a, 2, 4)
    print(reslt)
