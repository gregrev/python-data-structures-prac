def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # make empty list for full name list
    name_list = []
    # loop through the inputted dict list
    for name in people:
        # add the first and last name together using string literal
        full_name = f"{name['first']} {name['last']}"
        # add to name_list
        name_list.append(full_name)
    return name_list    