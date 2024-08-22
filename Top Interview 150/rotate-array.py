"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    """
    If we work on the same list we are going to have to slide the list one at a
    time.  
    """

    def rotate(self, nums: List[int], k: int) -> None:

        numsLenth = len(nums)
        
        if numsLenth == 1:
            # Simply return as the list will not change however much we rotate it. 
            return None

        if numsLenth < 1 or numsLenth > 100000:
            raise RuntimeError("Nums length is out of range, 1 to 100k") from None

        # declare a new list to move the items to. 
        numsRotated = [0]*numsLenth
        currentPosition = 0
        newPosition = 0

        # Rotate nums into a new list of the same length
        while currentPosition < numsLenth:
            newPosition = currentPosition + k

            while newPosition > numsLenth-1:
                # We will be outside the list 
                newPosition = newPosition - numsLenth            

            numsRotated[newPosition] = nums[currentPosition]
            currentPosition += 1

        currentPosition = 0

        # Write the roated values back to nums.
        while currentPosition < numsLenth:
            nums[currentPosition] = numsRotated[currentPosition]
            currentPosition +=1