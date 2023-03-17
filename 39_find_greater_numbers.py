def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # amount of times number is followed by bigger number
    amount = 0
    # interate over each index in the input
    for index in range(len(nums)):
        # iterate over each after the index
        for j in range(index+1, len(nums)):
            # check to see if index is less than j
            if nums[index] < nums[j]:
                # if yes add to amount
                amount += 1
    return amount