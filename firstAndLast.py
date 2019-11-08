def bsl(l,left,right,num):
    if right < left:
        return -1
    m = int((left+right)/2)
    if num > l[m]:
        return bsl(l,m+1,right,num)
    elif num < l[m]:
        return bsl(l,left,m-1,num)
    else:
        """we found num"""
        if m-1 == 0:
            return m
        if m-1 > 0 and l[m] != l[m-1]:
            return m
        return bsl(l,left,m-1,num)



def bsr(l,left,right,num):
    if right < left:
        return -1
    m = int((left + right) / 2)
    if num > l[m]:
        return bsr(l, m + 1, right, num)
    elif num < l[m]:
        return bsr(l, left, m - 1, num)
    else:
        """we found num"""
        if m + 1 == len(l):
            return m
        if m + 1 < len(l) and l[m] != l[m + 1]:
            return m
        return bsr(l, m+1, right, num)


def searchRange(l,num):
    left = bsl(l,0,len(l)-1,num)
    print(left)
    right = bsr(l,0,len(l)-1,num)
    print(right)


if __name__ == '__main__':
    l = [5,7,7,8,8,8,8,9,10]
    range = searchRange(l,8)