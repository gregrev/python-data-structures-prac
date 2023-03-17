def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # empty dict
    letter_count = {}
    # iterate over each letter in phrase
    for letter in phrase:
        # if letter is already in dict +1 that letter
        if letter in letter_count:
            letter_count[letter] += 1
        # if letter isnt in dict make it = 1
        else:
            letter_count[letter] = 1
    return letter_count #return the dict