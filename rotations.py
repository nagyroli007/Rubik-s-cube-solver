# Rotates the given side in the given direction (just those block are changed, that aro on the side)
def rotate_side(cube, side, clockvise):
    if clockvise:
        temp = cube[side][0]
        cube[side][0] = cube[side][3]
        cube[side][3] = cube[side][2]
        cube[side][2] = cube[side][1]
        cube[side][1] = temp
        temp = cube[side][4]
        cube[side][4] = cube[side][7]
        cube[side][7] = cube[side][6]
        cube[side][6] = cube[side][5]
        cube[side][5] = temp
    else:
        temp = cube[side][0]
        cube[side][0] = cube[side][1]
        cube[side][1] = cube[side][2]
        cube[side][2] = cube[side][3]
        cube[side][3] = temp
        temp = cube[side][4]
        cube[side][4] = cube[side][5]
        cube[side][5] = cube[side][6]
        cube[side][6] = cube[side][7]
        cube[side][7] = temp
    return cube


def rotate_U(cube):
    print("U ", end='')
    cube = rotate_side(cube, 0, True)
    seq = ((1, 0), (2, 0), (3, 0), (4, 0)), ((1, 4), (2, 4), (3, 4), (4, 4)), ((1, 1), (2, 1), (3, 1), (4, 1))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b + 1][0]][seq[i][b + 1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_U_counter(cube):
    print("U' ", end='')
    cube = rotate_side(cube, 0, False)
    seq = ((1, 0), (4, 0), (3, 0), (2, 0)), ((1, 4), (4, 4), (3, 4), (2, 4)), ((1, 1), (4, 1), (3, 1), (2, 1))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b + 1][0]][seq[i][b + 1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_L(cube):
    print("L ", end='')
    cube = rotate_side(cube, 1, True)
    seq = ((0, 0), (4, 2), (5, 0), (2, 0)), ((0, 7), (4, 5), (5, 7), (2, 7)), ((0, 3), (4, 1), (5, 3), (2, 3))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_L_counter(cube):
    print("L' ", end='')
    cube = rotate_side(cube, 1, False)
    seq = ((0, 0), (2, 0), (5, 0), (4, 2)), ((0, 7), (2, 7), (5, 7), (4, 5)), ((0, 3), (2, 3), (5, 3), (4, 1))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_F(cube):
    print("F ", end='')
    cube = rotate_side(cube, 2, True)
    seq = ((0, 2), (1, 1), (5, 0), (3, 3)), ((0, 6), (1, 5), (5, 4), (3, 7)), ((0, 3), (1, 2), (5, 1), (3, 0))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_F_counter(cube):
    print("F' ", end='')
    cube = rotate_side(cube, 2, False)
    seq = ((0, 2), (3, 3), (5, 0), (1, 1)), ((0, 6), (3, 7), (5, 4), (1, 5)), ((0, 3), (3, 0), (5, 1), (1, 2))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_R(cube):
    print("R ", end='')
    # Elforgatja a bal oldalt
    cube = rotate_side(cube, 3, True)
    # Forgatás sorrendjét elmentem (oldalakat)
    seq = ((0, 1), (2, 1), (5, 1), (4, 3)), ((0, 5), (2, 5), (5, 5), (4, 7)), ((0, 2), (2, 2), (5, 2), (4, 0))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_R_counter(cube):
    print("R' ", end='')
    # Elforgatja a bal oldalt
    cube = rotate_side(cube, 3, False)
    # Forgatás sorrendjét elmentem (oldalakat)
    seq = ((0, 1), (4, 3), (5, 1), (2, 1)), ((0, 5), (4, 7), (5, 5), (2, 5)), ((0, 2), (4, 0), (5, 2), (2, 2))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_B(cube):
    print("B ", end='')
    cube = rotate_side(cube, 4, True)
    seq = ((0, 0), (3, 1), (5, 2), (1, 3)), ((0, 4), (3, 5), (5, 6), (1, 7)), ((0, 1), (3, 2), (5, 3), (1, 0))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_B_counter(cube):
    print("B' ", end='')
    cube = rotate_side(cube, 4, False)
    seq = ((0, 0), (1, 3), (5, 2), (3, 1)), ((0, 4), (1, 7), (5, 6), (3, 5)), ((0, 1), (1, 0), (5, 3), (3, 2))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b+1][0]][seq[i][b+1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_D(cube):
    print("D ", end='')
    cube = rotate_side(cube, 5, True)
    seq = ((1, 3), (4, 3), (3, 3), (2, 3)), ((1, 6), (4, 6), (3, 6), (2, 6)), ((1, 2), (4, 2), (3, 2), (2, 2))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b + 1][0]][seq[i][b + 1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube


def rotate_D_counter(cube):
    print("D' ", end='')
    cube = rotate_side(cube, 5, False)
    seq = ((1, 3), (2, 3), (3, 3), (4, 3)), ((1, 6), (2, 6), (3, 6), (4, 6)), ((1, 2), (2, 2), (3, 2), (4, 2))
    for i in range(3):
        temp = cube[seq[i][0][0]][seq[i][0][1]]
        for b in range(3):
            cube[seq[i][b][0]][seq[i][b][1]] = cube[seq[i][b + 1][0]][seq[i][b + 1][1]]
        cube[seq[i][3][0]][seq[i][3][1]] = temp
    return cube