def bs(arr, left, right, num):
    if left > right:
        return -1

    mid = left + int((right-left)/2)
    if arr[mid] == num:
        return mid

    """ 
    We need to see where is the change point
    there are 2 cases
     l = [3,4,5,6,1,2]
     arr[mid] >= arr[left] change point is on the right as somwhere on right , as increasing array has decreased somewhere on right
     l = [5,6,1,2,3,4]
     arr[mid] < arr[left] change point is on left as right will always be increasing
     as if we start from 5 we can reach 2 only after a change
     
     Now lets say we are given a target
     if pivot is left and element is > arr[mid] but less than arr[left] then we need search the right side else left side
     if pivot is to right and element is < arr[mid] but > arr[right] we have to search on left side otherwise right
    
    """

    if arr[mid] < arr[left]:
        """
            pivot is left
        """
        if num > arr[mid] and num < arr[left]:
            return bs(arr, mid+1, right, num)
        else :
            return bs(arr, left, mid-1, num)
    else:
        """
            pivot is on right
        """
        if num < arr[mid] and num > arr[right]:
            return bs(arr, left, mid-1, num)
        else:
            return bs(arr, mid + 1, right, num)



def rotatedArray(l, num):
    return bs(l, 0, len(l)-1, num)



if __name__ == '__main__':
    l = [4,5,6,7,0,1,2,3]
    num = 5
    print(rotatedArray(l, num))
