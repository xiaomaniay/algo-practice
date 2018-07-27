class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        if not head or not head.next:
            return head
        p1, p, p2 = self.partition(head)
        sortedP1 = self.sortList(p1)
        sortedP2 = self.sortList(p2)

        p.next = sortedP2
        if not sortedP1:
            return p
        else:
            newHead = ListNode(0)
            newHead.next = sortedP1
            while sortedP1.next:
                sortedP1 = sortedP1.next
            sortedP1.next = p
            return newHead.next

    def partition(self, head):
        if not head:
            return None, None
        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        key = head.val
        while head:
            if head.val < key:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = p2.next = None
        p = head2.next
        head2.next = p.next
        p.next = None
        return head1.next, p, head2.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    a.next = b
    b.next = c
    reslt = Solution().sortList(a)
    print(reslt)

