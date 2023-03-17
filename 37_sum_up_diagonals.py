def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    #  value for diagonals
    diag1 = 0
    diag2 = 0
    
    # iterate over the rows of the matrix
    for index in range(len(matrix)):
        # add the element on the diagonal from top left to bottom right
        diag1 += matrix[index][index]
        # add the element on the diagonal from bottom left to top right
        diag2 += matrix[index][-index-1]
    
    # return the sum of the two diagonals
    return diag1 + diag2