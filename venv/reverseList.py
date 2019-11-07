class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def reverseList(head):
    """prev of first is null"""
    prev = None
    while head != None:
        """store next"""
        n = head.next
        """now we can point next to prev"""
        head.next = prev
        """prev is now head (1st iter prev will be 1)"""
        prev = head
        """head is now next (1st iter head will be 2)"""
        head = n

    return prev

def printList(root):
    while root:
        print(root.val)
        root = root.next


if __name__ == '__main__':
    first = ListNode(1)
    sec = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    first.next = sec
    sec.next = third
    third.next = fourth
    fourth.next = fifth
    root = reverseList(first)
    printList(root)