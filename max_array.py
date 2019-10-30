
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxAll = nums[0]
        currMax = nums[0]
        store = 0
        for i in range(1, len(nums)):
            """
            curMax is always the maximum value if you include the current element
            eg in below input
            [-2,1,-3,4,-1,2,1,-5,4]
            If you are at -3 and you include -3 then max will be max of (1+(-3) or -3)
            so currMax will be -2 -> (1+(-3)). But the max till that point is 1 which is                greater then -2..hence the overall max is still 1

            As we go forward if numbers are increasing then num + currMax will always be max
            note num + currMax is the max which includes current element... we need to find 
            max of all the currMaxes

            for eg lets iterate the above array
                    -2 currMax =-2
                    -2,1 currMax is now 1 [1]
                    -2,1,-3 currMax is not -2 [1,-3] or [-2]

                    Max is max(-2,1,-2) -> 1
            """
            currMax = max(nums[i] +currMax, nums[i])
            maxAll = max(maxAll, currMax)
            if currMax == maxAll:
                # at index i currMax is maxAll, so index i is part of maxAll and it is the last index of maxAll
                # also at end of all iteration the last currMax which is maxAll is the actual maxAll at index i
                # lets store this index where currMax is actually maxAll
                store = i

            temp = 0
            j = store
            while temp != maxAll:
                temp += nums[j]
                j = j-1



        print(maxAll)
        print("array is from "+str(j+1)+" to "+ str(store))


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol.maxSubArray(nums)
