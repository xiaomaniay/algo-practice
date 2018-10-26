
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head:
            return False
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    head = ListNode(0)
    head.next = head
    print(Solution().hasCycle(head))
