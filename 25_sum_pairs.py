def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # store numnbers in empty se 
    numbers = set()
    # iterate through inputted nums list
    for num in nums:
        # sum needed to reach goal
        goal_total = goal - num
        # Check if the target sum is in numbers set already
        if goal_total in numbers:
            # return a tuple with the pair of numbers that add up to the goal
            return (goal_total, num)
        #Add the current number to the set of numbers seen so far 
        numbers.add(num)
    #If no pair of numbers adds up to the goal, return an empty tuple 
    return ()




