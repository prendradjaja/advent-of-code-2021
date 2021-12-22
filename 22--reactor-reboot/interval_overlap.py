def interval_overlap(a, b):
    '''
      a 1----6
    >>> a = (1, 6)

    Cases where b[1] > a[1]
    -----------------------
      a 1----6
      b        8
    >>> interval_overlap(a, (8, 8))

      a 1----6
      b       78
    >>> interval_overlap(a, (7, 8))

      a 1----6
      b      6-8
    >>> interval_overlap(a, (6, 8))
    (6, 6)

      a 1----6
      b     5--8
    >>> interval_overlap(a, (5, 8))
    (5, 6)

      a 1----6
      b 1------8
    >>> interval_overlap(a, (1, 8))
    (1, 6)


    Cases where b[1] == a[1]
    ------------------------
      a 1----6
      b      6
    >>> interval_overlap(a, (6, 6))
    (6, 6)

      a 1----6
      b    4-6
    >>> interval_overlap(a, (4, 6))
    (4, 6)

      a 1----6
      b 1----6
    >>> interval_overlap(a, (1, 6))
    (1, 6)

    Cases where b[1] < a[1]
    ------------------------
      a 1----6
      b     5
    >>> interval_overlap(a, (5, 5))
    (5, 5)

      a 1----6
      b   3-5
    >>> interval_overlap(a, (3, 5))
    (3, 5)

      a 1----6
      b 1---5
    >>> interval_overlap(a, (1, 5))
    (1, 5)
    '''
    a, b = sorted([a, b])
    alo, ahi = a
    blo, bhi = b
    if blo > ahi:
        return None
    elif blo == ahi:
        return (blo, blo)
    else:
        hi = min(ahi, bhi)
        return (blo, hi)
