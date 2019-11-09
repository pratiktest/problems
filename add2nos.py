class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def add2nos(l1,l2):

    s1 = []
    s2 = []

    while l1:
        s1.append(l1.val)
        l1 = l1.next


    while l2:
        s2.append(l2.val)
        l2 = l2.next

    sum = 0
    carry = 0
    place = 1
    no1 = 0
    no2 = 0
    while s1 or s2:
        if not s1:
            no1 = 0
        else:
            no1 = s1.pop()
        if not s2:
            no2 = 0
        else:
            no2 = s2.pop()
        sum = int((carry + no1+no2)%10)*place + sum
        carry = int((no1+no2)/10)
        place = place*10

    print(sum)

if __name__ == '__main__':
    one1 = ListNode(1)
    two1 = ListNode(2)
    three1 = ListNode(3)

    one1.next = two1
    two1.next = three1

    one2 = ListNode(1)
    two2 = ListNode(3)
    three2 = ListNode(3)
    four2 = ListNode(9)

    one2.next = two2
    two2.next = three2
    three2.next = four2

    add2nos(one1, one2)

