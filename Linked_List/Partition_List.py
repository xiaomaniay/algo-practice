class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):

        # newHead = pre = ListNode(0)
        # pre.next = head
        # while head and head.val < x:
        #     pre = head
        #     head = head.next
        # while head and head.next:
        #     if head.next.val >= x:
        #         head = head.next
        #     else:
        #         temp = head.next
        #         head.next = temp.next
        #         temp.next = pre.next
        #         pre.next = temp
        #         pre = pre.next
        # return newHead.next
        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = head2.next
        p2.next = None
        return head1.next


if __name__ == "__main__":
    test = Solution()
    testList = ListNode(2)
    testList2 = ListNode(3)
    testList2.next = testList
    print(testList2)
    print(test.partition(testList2, 3))



