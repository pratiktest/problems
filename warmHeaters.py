
def findRadius(houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    heaters.sort()
    houses.sort()

    """
        2 pointer method
        Now we iterate over the houses
        idea is to find NEAREST HEATER FOR EACH HOUSE
        1,2,3,4,5,6,7,8
        1,2,5,30
        
        nearest heater for 1 is 1
        for 2 is 2
        for 3 is 2
        for 4 is 5
        for 5 is 5...
        for 8 is 5
        
        as we go on moving the pointer we will see that the dist we need is atleast 
        the distance between heater and the house
    """
    i = 0
    j = 0
    res = 0

    while i < len(houses):
        while j < len(heaters)-1 and abs(heaters[j+1]-houses[i]) <= abs(heaters[j]-houses[i]):
            j = j+1
        res = max(res, abs(heaters[j] - houses[i]))
        i = i+1

    return res


if __name__ == '__main__':
    houses = [1, 2, 3, 4, 5, 6, 7, 8]
    heaters = [2, 5, 30, 1]
    findRadius(houses,heaters)
