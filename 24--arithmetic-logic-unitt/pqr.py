pattern = '''
inp w
mul x 0
add x z
mod x 26
div z N
add x N
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y N
mul y x
add z y
'''.strip().split('\n')

lines = [line.rstrip('\n') for line in open('in')]
for i in range(14):
    chunk = lines[i * 18:(i+1)*18]
    for exp, act in zip(pattern, chunk):
        if 'N' in exp:
            print(act.split()[-1],end='\t')
            continue
        if exp != act:
            1/0
    print()
