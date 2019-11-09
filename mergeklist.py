

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def merge2list(l1,l2):
    res = ListNode(0)
    head = res
    while l1 or l2:
        if not l1:
            res.next = l2
            break
        if not l2:
            res.next = l1
            break
        if l1.val <= l2.val:
            res.next = ListNode(l1.val)
            res = res.next
            l1 = l1.next
        else:
            res.next = ListNode(l2.val)
            res = res.next
            l2 = l2.next

    return head.next

def mergeklist(klist):
    length = len(klist)
    """
        interval = 1
        range is from 0 to 3-1 . i.e 2
        so i = 0 we merge 0 and 1 into 0
        i = 2 but 2<2 is false so we break
        
        interval becomes 2
        amount -interval = 1
        i = 0 and i+2-> 2
        merge 0 and 2
        
        bottomline
        we always go in multiples of 2 as 0 and 1 is merged in 0
        2 and 3 is merged in 2
        so next time i will merge 0 and 2 so increment i by interval*2
        
        if interval is 2 then we merge 0 and 2...4 and 6 (as before 0,1->0
        and 2,3->2 4,5->4 6,7->6 so we need to merge 0,2 and 4,6
        
        hence i = i + interval*2
        
        if we increment by 1 it will go 0,1 2,3 4,5 it will go till 5
        as 4 and 5 merge into 5 now in next iteration we need to go only till 4
        if we increment by 2 it will go till 6-2 = 4 -> 0,2 ...4
        if we increment by 3 it will go till 6-3 = 3 0->4
        
        so always it will go till length-interval
        
    """
    interval = 1
    while interval < length:
        for i in range(0, length-interval, interval*2):
            klist[i] = merge2list(klist[i], klist[i+interval])
    interval = interval*2

    return klist[0]






if __name__ == '__main__':
    one1 = ListNode(1)
    two1 = ListNode(2)
    three1 = ListNode(3)

    one1.next = two1
    two1.next = three1

    one2 = ListNode(1)
    two2 = ListNode(3)
    three2 = ListNode(4)

    one2.next = two2
    two2.next = three2

    one3 = ListNode(2)
    two3 = ListNode(6)

    one3.next = two3

    mergeklist([one1, one2, one3])