import itertools

onetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9]

q = {
    1: 13,
    2: 12,
    3: 12,
    4: 10,
    5: -11,
    6: -13,
    7: 15,
    8: 10,
    9: -2,
    10: -6,
    11: 14,
    12: 0,
    13: -15,
    14: -4
}
r = {
    1: 8,
    2: 13,
    3: 8,
    4: 10,
    5: 12,
    6: 1,
    7: 13,
    8: 5,
    9: 10,
    10: 3,
    11: 2,
    12: 2,
    13: 12,
    14: 7
}

def backbig(q, r, z_after, w):
    '''
    Find w and z_before
    '''
    results = []
    z_before = z_after * 26 + (w - q)
    return z_before

def backsmall(q, r, z_after):
    z = z_after
    w = z - 26 * (z // 26) - r
    if w not in onetonine:
        return None
    return w, z//26

def main():
    i = 0
    za14 = 0
    result = None
    results = []
    for w14 in onetonine:
        za13 = backbig(q[14], r[14], za14, w14)
        for w13 in onetonine:
            za12 = backbig(q[13], r[13], za13, w13)
            for w12 in onetonine:
                za11 = backbig(q[12], r[12], za12, w12)

                x = backsmall(q[11], r[11], za11) #,w11
                if not x: continue
                w11, za10 = x

                for w10 in onetonine:
                    za9 = backbig(q[10], r[10], za10, w10)
                    for w9 in onetonine:
                        za8 = backbig(q[9], r[9], za9, w9)

                        x = backsmall(q[8], r[8], za8) #,w8
                        if not x: continue
                        w8, za7 = x

                        x = backsmall(q[7], r[7], za7) #,w7
                        if not x: continue
                        w7, za6 = x

                        for w6 in onetonine:
                            za5 = backbig(q[6], r[6], za6, w6)

                            for w5 in onetonine:
                                za4 = backbig(q[5], r[5], za5, w5)

                                x = backsmall(q[4], r[4], za4) #,w4
                                if not x: continue
                                w4, za3 = x

                                x = backsmall(q[3], r[3], za3) #,w3
                                if not x: continue
                                w3, za2 = x

                                x = backsmall(q[2], r[2], za2) #,w2
                                if not x: continue
                                w2, za1 = x

                                x = backsmall(q[1], r[1], za1) #,w1
                                if not x: continue
                                w1, za0 = x

                                assert za0 == 0
                                # result = (w1, za0)
                                results.append((w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14))
    for each in sorted(results):
        print(each)

main()
