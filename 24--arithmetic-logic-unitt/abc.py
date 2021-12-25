abc = 'abcdefghijklmnopqrstuvwxyz'

for line in '''13	8
12	13
12	8
10	10
-11	12
-13	1
15	13
10	5
-2	10
-6	3
14	2
0	2
-15	12
-4	7'''.split('\n'):
    a, b = line.split()
    a = int(a)
    b = int(b)
    print(abc[(a+b)%26])

