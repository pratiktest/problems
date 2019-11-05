
def hammingDistance(n1,n2):
    """
    perform an or operation
    0 0 0 1 (1)
    0 1 0 0 (4)

    doing an xor on above we will get the difference
    1 ^ 1 = 0
    0 ^ 0 = 0
    so we will get 1's in places where digits are different
    0 1 0 1

    Then and them with 1 to get number of 1's and right shift
    till the number becomes 0
    basically count number of 1's..

    NUMBER OF 1's is HAMMING DISTANCE
    """
    x = n1 ^ n2
    setBits = 0
    while x>0:
        y = x&1
        setBits = setBits + y
        x = x>>1

    return setBits


if __name__ == '__main__':
    x = 1
    y = 4
    dist = hammingDistance(1,4)
    print(dist)

