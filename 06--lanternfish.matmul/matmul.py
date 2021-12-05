def matmul(a,b):
    '''
    >>> A = [[1, 2, 3]]
    >>> B = [[4], [5], [6]]
    >>> matmul(A, B)
    [[32]]

    >>> BA_expected = [
    ...     [4, 8, 12],
    ...     [5, 10, 15],
    ...     [6, 12, 18],
    ... ]
    >>> matmul(B, A) == BA_expected
    True

    Copied from https://stackoverflow.com/a/48597323/1945088
    '''
    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    return c

