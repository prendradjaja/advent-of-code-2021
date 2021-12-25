def solve(p, q, r, z_after):
    '''
    Find w and z_before
    '''
    if p == 26:
        w = 9
        z_before = z_after * 26 + (w - q)
        return { 'w': w, 'z_before': z_before }

# print(solve(26, -4, 7, 0))
print(solve(26, -11, 12, 9426))
