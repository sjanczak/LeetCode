"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
class Solution:
    """
    Iterate through the list forwards and backwards checking the previous ratings and candy allocations
    A chain of higher ratings left to right will mean the candy allocation will increase.
    A chain of higher ratings right to left will also mean the candy allocations will increase in
    reverse.
    """
    def candy(self, ratings: List[int]) -> int:
        noOfChildren = len(ratings)
        candyAllocations = [0]*noOfChildren

        if noOfChildren == 1:
            candyAllocations[0] = 1
        else:

            # Reset local variables
            previousRating = -1
            nextRating = -1
            nextRatingAlocation = -1

            ratingPosition = 0
            
            """
            Forward traverse the ratings to find the increases left to right.
            """
            while ratingPosition < noOfChildren:
                currentRating = ratings[ratingPosition]

                if ratingPosition == 0:
                    # Start of the list is always 1
                    candyAllocations[ratingPosition] = 1
                else:
                    previousRating = ratings[ratingPosition - 1]

                    if previousRating < currentRating:
                        # We need to give 1 more candy allocation than th previous.
                        candyAllocations[ratingPosition] = candyAllocations[ratingPosition - 1] + 1
                    else:
                        candyAllocations[ratingPosition] = 1

                ratingPosition += 1 

            # Reset local variables
            currentRating = -1
            currentCandyAllocation = -1
            previousRating = -1
            previousCandyAlocation = -1

            ratingPosition = noOfChildren - 1
            
            """
            Now reverse traverse the ratings to find the increases right to left.
            """
            while ratingPosition >= 0:
                currentRating = ratings[ratingPosition]
                currentCandyAllocation = candyAllocations[ratingPosition]

                if ratingPosition != 0:
                    previousRating = ratings[ratingPosition - 1]

                    if currentRating < previousRating:
                        previousCandyAlocation = candyAllocations[ratingPosition - 1]
                        if previousCandyAlocation <= currentCandyAllocation:
                            # We need to increase the previous candy allocation.
                            candyAllocations[ratingPosition - 1] = currentCandyAllocation + 1

                ratingPosition -= 1 
            
        return sum(candyAllocations)
            
