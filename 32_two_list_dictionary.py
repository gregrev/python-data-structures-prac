def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    # empty dict
    result = {}

    # iterate through the keys
    for i, key in enumerate(keys):
        # check if there are any values left
        if i < len(values):
            # if there is a value, add it to the dictionary
            result[key] = values[i]
        else:
            # if there is no value, add None to the dictionary
            result[key] = None

    # return the result
    return result