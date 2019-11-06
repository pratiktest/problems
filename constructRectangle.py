import math

def constructRectangle(area):

    w = 1
    l = area
    mindiff = area - 1

    """
     if area = 5 math.sqrt is going to be 2..
     length >= width so we take width from 2 to math.sqrt
     since after that width will be > length
     
     eg 20
     sqrt(20) = 4
     so width can be max 4  as after that it will be > length -> after that width will be 5 which will violate length>=width
     
    """
    sqrt = int(math.sqrt(area))
    print(sqrt)
    ## sqrt+1 is because of end is not in range
    for i in range(2, sqrt+1):
        """
            if area is divisible by i(width) then we can make a i*j = area
        """
        if area % i == 0:
            diff = area/i - i
        if diff < mindiff:
            mindiff = diff
            w = i
            l = int(area/i)

    return [l,w]

if __name__ == '__main__':
    area = 4
    rect = constructRectangle(area)
    print(rect)