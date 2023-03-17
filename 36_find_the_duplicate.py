def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    # store numbers in a set
    dupe = set()

    # iterate through nums
    for num in nums:
        # if num is in the dupe set return that number, ends there
        if num in dupe:
            return num
        # if not thereadd that num o the dupe set 
        else:
            dupe.add(num)
    #if all numbers are added to the set and no dupe return none
    return None
