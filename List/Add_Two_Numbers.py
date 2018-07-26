class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # newHead = pre = ListNode(0)
        # pre.next = l1
        # increment = 0
        # while l1 and l2:
        #     l1.val += (l2.val + increment)
        #     increment = 0
        #     while l1.val > 9:
        #         increment += 1
        #         l1.val -= 10
        #     pre = l1
        #     if not l1.next and l2.next:
        #         l1.next = ListNode(0)
        #     if not l2.next and l1.next:
        #         l2.next = ListNode(0)
        #     l1 = l1.next
        #     l2 = l2.next
        # if increment > 0:
        #     if pre.next:
        #         pre.next.val += increment
        #     else:
        #         pre.next = ListNode(increment)
        newHead = pre = ListNode(0)
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            pre.next = ListNode(val)
            pre = pre.next
        if carry > 0:
            pre.next = ListNode(carry)
        return newHead.next

if __name__ == "__main__":
    l1 = ListNode(9)
    a = ListNode(1)
    b = ListNode(3)
    l1.next = a
    a.next = b
    l2 = ListNode(9)
    c = ListNode(9)
    l2.next = c
    reslt = Solution().addLists(l2, l1)
    while reslt:
        print(reslt.val)
        reslt = reslt.next


