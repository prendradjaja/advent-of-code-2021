Alternate solution using matrix multiplication and exponentiation by squaring.

Explanation:
------------
We have a matrix (`step`) that can be used to move the simulation forward one
day. Since matrix multiplication is associative, we can also use the nth power
of `step` to move the simulation forward n days.

Exponentiation by squaring can be used to compute an nth power in O(log(n))
multiplications.


Findings:
---------
Unfortunately, we don't generally get a performance advantage by using this
approach, because for large n the (i.e. this is not an O(log(n)) algorithm)
matrix elements become very large and each matrix multiplication step becomes
very slow.

That said, if the question is modified slightly to avoid runaway growth of
matrix elements, this technique *would* result in an O(log(n)) algorithm,
e.g.:

- If we're only interested in the fish count mod e.g. 1000, then we can use
  modulo for matrix elements as well (main_alt.py)
- If the `step` matrix had a "growth factor" of 1 or approximately 1


See also: https://gist.github.com/rain-1/51944f4ed9318c320cfa0af2a03e6808
