class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def rotate(head, k):
    pointer = head
    i = 1
    # find where the head will advance
    while i <= k:
        pointer = pointer.next
        if not pointer:
            pointer = head
        i = i+1

    # head will be at pointer after k rotations
    # so now we need to find distance between pointer and head. This will help us find new head
    # as head will advance pointer-head spaces, we will have to find some node that will advance pointer-head
    # spaces and become the new head. This node is exactly pointer-head spaces from the last node...
    # as head proceeds pointer-head spaces...this node will proceed pointer-head spaces and get pushed to the top(head)
    # of the list..the node exactly before this node will be pushed to the tail so mark these two nodes

    curr_head = head
    i = 0
    while curr_head != pointer:
        curr_head = curr_head.next
        i = i+1

    slow = head
    fast = head
    new_tail = head
    curr_tail = head
    slow_start = False
    j = 0
    while fast:
        if not fast.next:
            curr_tail = fast
        fast = fast.next
        if slow_start:
            new_tail = new_tail.next
        if j >= i:
            slow = slow.next
            slow_start = True
        j = j+1

    if not slow:
        return head

    # slow is the new head
    curr_tail.next = head
    head = slow
    new_tail.next = None

    pointer = head
    while pointer:
        print(pointer.val)
        pointer = pointer.next

    return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    rotate(l1, 10)


