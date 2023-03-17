def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # split the string into a list where each word is a list item with .split()
    phrase = phrase.split()
    # capitalize the first list item (word)
    if phrase:
        phrase[0] = phrase[0].capitalize()
        # make list back into a string with join()
    return ' '.join(phrase)