rotators2d = {
    0: lambda point: (point[0], point[1]),
    1: lambda point: (point[1], -point[0]),
    2: lambda point: (-point[0], -point[1]),
    3: lambda point: (-point[1], point[0]),
}


rotators3d = {
    0:  lambda point: (point[0], point[1], point[2]),
    1:  lambda point: (point[2], point[1], -point[0]),
    2:  lambda point: (-point[0], point[1], -point[2]),
    3:  lambda point: (-point[2], point[1], point[0]),
    4:  lambda point: (point[0], point[2], -point[1]),
    5:  lambda point: (point[2], -point[0], -point[1]),
    6:  lambda point: (-point[0], -point[2], -point[1]),
    7:  lambda point: (-point[2], point[0], -point[1]),
    8:  lambda point: (point[1], point[2], point[0]),
    9:  lambda point: (point[1], -point[0], point[2]),
    10: lambda point: (point[1], -point[2], -point[0]),
    11: lambda point: (point[1], point[0], -point[2]),
    12: lambda point: (-point[0], point[2], point[1]),
    13: lambda point: (-point[2], -point[0], point[1]),
    14: lambda point: (point[0], -point[2], point[1]),
    15: lambda point: (point[2], point[0], point[1]),
    16: lambda point: (-point[1], point[2], -point[0]),
    17: lambda point: (-point[1], -point[0], -point[2]),
    18: lambda point: (-point[1], -point[2], point[0]),
    19: lambda point: (-point[1], point[0], point[2]),
    20: lambda point: (-point[2], -point[1], -point[0]),
    21: lambda point: (point[0], -point[1], -point[2]),
    22: lambda point: (point[2], -point[1], point[0]),
    23: lambda point: (-point[0], -point[1], point[2]),
}
