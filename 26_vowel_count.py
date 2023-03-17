def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # set the vowels
    vowels = set('aeiou')
    # make empty dict
    count = {}
    # iterate over each letter in phrase while lower case
    for char in phrase.lower():
        # if letter is in vowels
        if char in vowels:
            # add char as a key in the count dict
            # if char is not in freq, it gets
            # added with a value of 0 gets incremented
            count[char] = count.get(char, 0) + 1
            # return the dict
    return count