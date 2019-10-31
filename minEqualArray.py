
def brute_force():
    nums = [1, 2, 10]
    s = set()
    maximum = nums[0]
    minimum = nums[0]
    max_index = 0
    min_index = 0
    for i in range(1, len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
            max_index = i
        if nums[i] < minimum:
            minimum = nums[i]
            min_index = i
        s.add(nums[i])

    if len(s) == 1:
        print(0)

    new_max_index = max_index
    no = 1
    while True:
        s = set()
        for i in range(0, len(nums)):
            if i != max_index:
                nums[i] = nums[i] + 1
            if nums[i] > nums[max_index]:
                new_max_index = i
            s.add(nums[i])
        if len(s) == 1:
            break
        no = no + 1
        max_index = new_max_index

    print(no)

def sort():
    nums = [1, 2, 10]
    """sort the numbers"""
    nums.sort()
    i = len(nums) - 1
    moves = 0
    """
    always the last number will now be the biggest
    For smallest number to get to largest number we need to make diff = nums[last] - nums[0] moves
    since sorted nums[last] will be largest
    
    Once nums[0] is moved to max by doing diff number of  moves, 
    so now the second largest element will be largest after diff moves.
    nums[0] will still be smallest but now it has to catch up with the new largest element (second largest) nums[last-1]
    For this nums[0] will have to make diff = nums[last-1] - nums[0] moves
    
    After which the third last element will be the largest and this will go on for all array
    """
    while i>0:
        diff = nums[i] - nums[0]
        moves = moves + diff
        i = i-1

    print(moves)




if __name__  == '__main__':
   brute_force()
   sort()

