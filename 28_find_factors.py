def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # empy list to store factors
    factors = []
    # iterate over numers from 1 to num
    for fact in range(1, num + 1):
        # if its a factor add to factors list
        if num % fact == 0:
            factors.append(fact)
            # return the list
    return factors  
