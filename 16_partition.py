def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # make empty lists
    
    a_list = []
    b_list = []

    # loop through inputted list
    for elem in lst:
        # if the current elem is true append to a list
        if fn(elem):
            a_list.append(elem)
            # otherwise add to b lsit
        else:
            b_list.append(elem)
        # return list
    return [a_list, b_list]