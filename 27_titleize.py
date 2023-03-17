def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    # words = phrase.split()
    # capitalized_words = []
    # for word in words:
    #     capitalized_word = word.capitalize()
    #     capitalized_words.append(capitalized_word)
    # return ' '.join(capitalized_words)    

    return ' '.join(word.capitalize() for word in phrase.split())