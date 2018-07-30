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
        tail = self.getTail(head)
        head, tail = self.quickSort(head, tail)
        return head

    def quickSort(self, head, tail):

        leftHead, leftTail, midHead, midTail, rightHead, rightTail = self.partition(head, tail)

        if leftHead:
            leftHead, leftTail = self.quickSort(leftHead, leftTail)
            leftTail.next = midHead
        else:
            leftHead = midHead
        if rightHead:
            rightHead, rightTail = self.quickSort(rightHead, rightTail)
            midTail.next = rightHead
            rightTail.next = None
        else:
            rightTail = midTail
            midTail.next = None
        return leftHead, rightTail

    def partition(self, head, tail):
        pivotNode = head
        midHead = midTail = pivotNode
        leftHead = leftTail = rightHead = rightTail = None
        while head.next and head is not tail:
            head = head.next
            if head.val < pivotNode.val:
                if not leftHead:
                    leftHead = head
                    leftTail = head
                else:
                    leftTail.next = head
                    leftTail = head
            elif head.val > pivotNode.val:
                if not rightHead:
                    rightHead = head
                    rightTail = head
                else:
                    rightTail.next = head
                    rightTail = head
            else:
                midTail.next = head
                midTail = head

        return leftHead, leftTail, midHead, midTail, rightHead, rightTail

    def getTail(self, head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail


if __name__ == "__main__":
    a = ListNode(0)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(-1)
    a.next = b
    b.next = c
    c.next = d
    reslt = Solution().sortList(a)
    print(reslt)

