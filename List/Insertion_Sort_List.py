class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        newHead = ListNode(0)
        newHead.next = head
        count = 0
        while head:
            count += 1
            insertPoint = newHead.next
            count2 = 0
            while insertPoint and insertPoint.val < head.val:
                count2 += 1
                insertPoint = insertPoint.next
            temp = insertPoint.val
            insertPoint.val = head.val
            for i in range(count - count2 - 1):
                temp2 = insertPoint.next.val
                insertPoint.next.val = temp
                temp = temp2
                insertPoint = insertPoint.next
            head = head.next
        return newHead.next


if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(3)
    c = ListNode(1)
    d = ListNode(8)
    e = ListNode(5)
    f = ListNode(11)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    reslt = Solution().insertionSortList(a)
    while reslt:
        print((reslt.val))
        reslt = reslt.next


