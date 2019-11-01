def bruteForce():
    greed_factor = [2, 7, 5]
    cookie_size = [3, 9]

    greed_factor.sort()
    cookie_size.sort()

    """
    [2,5,7] and [3,9]
    after sorting we can be greedy as 9 biggest size will be given to most greediest child
    simplest case is -> [1,2,3], [1,1]
    give 1 to 1 and thats all we can do ..so answer is 1
    [4,2,3,4,1,10] [3,2,1,8,12]
    we can give 3 to 2... 1to1... 8 to 4...12to10
    OR
    we can give 3 to 3..2 to 2...1 to 1...8 to 4...12 to 10... and we satisfy more kids
    """
    print(greed_factor)
    min_diff = 10000
    minIndex = None
    satisfied = 0
    for i in range(0, len(cookie_size)):

        for j in range(0, len(greed_factor)):
            if cookie_size[i] > greed_factor[j]:
                diff = cookie_size[i] - greed_factor[j]
                if diff < min_diff:
                    min_diff = diff
                    minIndex = j

        if minIndex is not None:
            satisfied = satisfied + 1
            del greed_factor[minIndex]
            min_diff = 10000
            minIndex = None

    print(satisfied)

def sort():
    """
    We can sort both arrays and then compare. (comparison always think of sorting)
    we will compare the biggest cookie with the greediest child and see if we can satisfy him
    If we cant then we will try to go to 2nd greediest child..
    If we cannot satisy the greediest child no other cookie can satisfy as there is no cookie
    bigger than the last so we just move pointers instead of removing the elements..hence
    this is most optimized and can be done in O(n+m) rather than O(nm)
    Just we will need to sort nlogn +mlogm
    :return:
    """
    greed_factor = [2, 7, 5]
    cookie_size = [3, 9]

    greed_factor.sort()
    cookie_size.sort()

    i = len(cookie_size) -1
    j = len(greed_factor) -1
    satisfied = 0

    while i>=0 and j>=0:
        if cookie_size[i] >= greed_factor[j]:
            satisfied = satisfied + 1
            i = i-1
            j = j-1
        else:
            j = j-1

    print(satisfied)



if __name__ == '__main__':
    bruteForce()
    sort()

