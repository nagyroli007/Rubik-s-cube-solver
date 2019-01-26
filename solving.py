import rotations


def is_edge_buffer(cube):
    a = cube[0][5]
    b = cube[3][4]
    if (a == 'w' and b == 'r') or (a == 'r' and b == 'w'):
        return True
    return False


def is_edges_solved(cube):
    for s in range(6):
        for b in range(4, 8):
            if cube[s][b] != cube[s][8]:
                return False
    return True


def is_corner_buffer(cube):
    a = cube[1][0]
    b = cube[0][0]
    c = cube[4][1]
    abc = a + b + c
    if abc == 'owb' or abc == 'bow' or abc == 'wbo':
        return True
    return False


def is_corners_solved(cube):
    for s in range(6):
        for b in range(4):
            if cube[s][b] != cube[s][8]:
                return False
    return True


def bring_edge_to_change(cube, a, b):
    if a == 'w':
        if b == 'b':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
        elif b == 'o':
            return cube
        elif b == 'g':
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
    elif a == 'o':
        if b == 'w':
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_U_counter(cube)
        elif  b == 'g':
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_F(cube)
            cube = rotations.rotate_U(cube)
        elif b == 'y':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_U_counter(cube)
        elif b == 'b':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_U_counter(cube)
    elif a == 'g':
        if b == 'w':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_F_counter(cube)
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_R_counter(cube)
        elif b == 'r':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
        elif b == 'y':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_F(cube)
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_R_counter(cube)
        elif b == 'o':
            cube = rotations.rotate_L_counter(cube)
    elif a == 'r':
        if b == 'b':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_U_counter(cube)
        elif b == 'y':
            cube = rotations.rotate_D_counter(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_F(cube)
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_R_counter(cube)
        elif b == 'g':
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_F_counter(cube)
            cube = rotations.rotate_U(cube)
    elif a == 'b':
        if b == 'w':
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'o':
            cube = rotations.rotate_L(cube)
        elif b == 'y':
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'r':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
    elif a == 'y':
        if b == 'g':
            cube = rotations.rotate_D_counter(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'r':
            cube = rotations.rotate_D(cube)
            cube = rotations.rotate_D(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'b':
            cube = rotations.rotate_D(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'o':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
    return cube


def bring_edge_back(cube, a, b):
    if a == 'w':
        if b == 'b':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
        elif b == 'o':
            return cube
        elif b == 'g':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_R(cube)
    elif a == 'o':
        if b == 'w':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_L(cube)
        elif b == 'g':
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_F_counter(cube)
            cube = rotations.rotate_U(cube)
        elif b == 'y':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_L_counter(cube)
        elif b == 'b':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_U_counter(cube)
    elif a == 'g':
        if b == 'w':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_F(cube)
            cube = rotations.rotate_R_counter(cube)
        elif b == 'r':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
        elif b == 'y':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_F_counter(cube)
            cube = rotations.rotate_R_counter(cube)
        elif b == 'o':
            cube = rotations.rotate_L(cube)
    elif a == 'r':
        if b == 'b':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_U_counter(cube)
        elif b == 'y':
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_F_counter(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_D(cube)
        elif b == 'g':
            cube = rotations.rotate_U_counter(cube)
            cube = rotations.rotate_F(cube)
            cube = rotations.rotate_U(cube)
    elif a == 'b':
        if b == 'w':
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_B_counter(cube)
            cube = rotations.rotate_R(cube)
        elif b == 'o':
            cube = rotations.rotate_L_counter(cube)
        elif b == 'y':
            cube = rotations.rotate_L_counter(cube)
            cube = rotations.rotate_R_counter(cube)
            cube = rotations.rotate_B(cube)
            cube = rotations.rotate_R(cube)
        elif b == 'r':
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_R(cube)
            cube = rotations.rotate_U(cube)
            cube = rotations.rotate_U(cube)
    elif a == 'y':
        if b == 'g':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_D(cube)
        elif b == 'r':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_D(cube)
            cube = rotations.rotate_D(cube)
        elif b == 'b':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_D_counter(cube)
        elif b == 'o':
            cube = rotations.rotate_L(cube)
            cube = rotations.rotate_L(cube)
    return cube


def change_edges(cube):
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_F(cube)
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_F_counter(cube)
    return cube


def bring_corner_to_change(cube, a, b, c):
    abc = a + b + c
    if abc == 'owb' or abc == 'bow' or abc == 'wbo':
        return cube
    elif abc == 'wrb':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'wog':
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'wgr':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_D_counter(cube)
    elif abc == 'ogw':
        cube = rotations.rotate_F_counter(cube)
        cube = rotations.rotate_D(cube)
    elif abc == 'oyg':
        cube = rotations.rotate_F_counter(cube)
    elif abc == 'oby':
        cube = rotations.rotate_D_counter(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'gwo':
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'grw':
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'gyr':
        cube = rotations.rotate_F_counter(cube)
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'goy':
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'rwg':
        cube = rotations.rotate_F(cube)
    elif abc == 'rbw':
        cube = rotations.rotate_R_counter(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'ryb':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'rgy':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'bwr':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_D_counter(cube)
    elif abc == 'byo':
        cube = rotations.rotate_D(cube)
        cube = rotations.rotate_F_counter(cube)
    elif abc == 'bry':
        cube = rotations.rotate_R(cube)
    elif abc == 'ygo':
        cube = rotations.rotate_D(cube)
    elif abc == 'yrg':
        return cube
    elif abc == 'ybr':
        cube = rotations.rotate_D_counter(cube)
    elif abc == 'yob':
        cube = rotations.rotate_D(cube)
        cube = rotations.rotate_D(cube)
    return cube


def bring_corner_back(cube, a, b, c):
    abc = a + b + c
    if abc == 'owb' or abc == 'bow' or abc == 'wbo':
        return cube
    elif abc == 'wrb':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'wog':
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'wgr':
        cube = rotations.rotate_D(cube)
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'ogw':
        cube = rotations.rotate_D_counter(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'oyg':
        cube = rotations.rotate_F(cube)
    elif abc == 'oby':
        cube = rotations.rotate_R_counter(cube)
        cube = rotations.rotate_D(cube)
    elif abc == 'gwo':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_F_counter(cube)
    elif abc == 'grw':
        cube = rotations.rotate_R(cube)
    elif abc == 'gyr':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'goy':
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_F(cube)
    elif abc == 'rwg':
        cube = rotations.rotate_F_counter(cube)
    elif abc == 'rbw':
        cube = rotations.rotate_F_counter(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'ryb':
        cube = rotations.rotate_F_counter(cube)
        cube = rotations.rotate_R(cube)
        cube = rotations.rotate_R(cube)
    elif abc == 'rgy':
        cube = rotations.rotate_F_counter(cube)
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'bwr':
        cube = rotations.rotate_D(cube)
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'byo':
        cube = rotations.rotate_F(cube)
        cube = rotations.rotate_D_counter(cube)
    elif abc == 'bry':
        cube = rotations.rotate_R_counter(cube)
    elif abc == 'ygo':
        cube = rotations.rotate_D_counter(cube)
    elif abc == 'yrg':
        return cube
    elif abc == 'ybr':
        cube = rotations.rotate_D(cube)
    elif abc == 'yob':
        cube = rotations.rotate_D(cube)
        cube = rotations.rotate_D(cube)
    return cube


def change_corners(cube):
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_F_counter(cube)
    cube = rotations.rotate_R(cube)
    cube = rotations.rotate_U(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_U_counter(cube)
    cube = rotations.rotate_R_counter(cube)
    cube = rotations.rotate_F(cube)
    cube = rotations.rotate_R(cube)
    return cube


def get_block_colors(a, b):
    colors = ['', '']
    c_code = ('w', 'o', 'g', 'r', 'b', 'y')
    colors[0] = c_code[a]
    if a == 0:
        if b == 4:
            colors[1] = 'b'
        elif b == 5:
            colors[1] = 'r'
        elif b == 6:
            colors[1] = 'g'
        elif b == 7:
            colors[1] = 'o'
    elif a == 1:
        if b == 4:
            colors[1] = 'w'
        elif b == 5:
            colors[1] = 'g'
        elif b == 6:
            colors[1] = 'y'
        elif b == 7:
            colors[1] = 'b'
    elif a == 2:
        if b == 4:
            colors[1] = 'w'
        elif b == 5:
            colors[1] = 'r'
        elif b == 6:
            colors[1] = 'y'
        elif b == 7:
            colors[1] = 'o'
    elif a == 3:
        if b == 4:
            colors[1] = 'w'
        elif b == 5:
            colors[1] = 'b'
        elif b == 6:
            colors[1] = 'y'
        elif b == 7:
            colors[1] = 'g'
    elif a == 4:
        if b == 4:
            colors[1] = 'w'
        elif b == 5:
            colors[1] = 'o'
        elif b == 6:
            colors[1] = 'y'
        elif b == 7:
            colors[1] = 'r'
    elif a == 5:
        if b == 4:
            colors[1] = 'g'
        elif b == 5:
            colors[1] = 'r'
        elif b == 6:
            colors[1] = 'b'
        elif b == 7:
            colors[1] = 'o'
    return colors


def get_corner_colors(a, b):
    if a == 0:
        if b == 0:
            return 'wbo'
        if b == 1:
            return 'wrb'
        if b == 2:
            return 'wgr'
        if b == 3:
            return 'wog'
    if a == 1:
        if b == 0:
            return 'owb'
        if b == 1:
            return 'ogw'
        if b == 2:
            return 'oyg'
        if b == 3:
            return 'oby'
    if a == 2:
        if b == 0:
            return 'gwo'
        if b == 1:
            return 'grw'
        if b == 2:
            return 'gyr'
        if b == 3:
            return 'goy'
    if a == 3:
        if b == 0:
            return 'rwg'
        if b == 1:
            return 'rbw'
        if b == 2:
            return 'ryb'
        if b == 3:
            return 'rgy'
    if a == 4:
        if b == 0:
            return 'bwr'
        if b == 1:
            return 'bow'
        if b == 2:
            return 'byo'
        if b == 3:
            return 'bry'
    if a == 5:
        if b == 0:
            return 'ygo'
        if b == 1:
            return 'yrg'
        if b == 2:
            return 'ybr'
        if b == 3:
            return 'yob'


def solve(cube):
    print("Solving: ", end='')
    while not is_edges_solved(cube):
        if not is_edge_buffer(cube):
            cube = bring_edge_to_change(cube, cube[0][5], cube[3][4])
            cube = change_edges(cube)
            cube = bring_edge_back(cube, cube[0][7], cube[1][4])
        else:
            quit = False
            for s in range(6):
                if not quit:
                    for b in range(4, 8):
                        if cube[s][b] != cube[s][8]:
                            colors = get_block_colors(s, b)
                            if not ((colors[0] == 'w' and colors[1] == 'r') or (colors[1] == 'w' and colors[0] == 'r')):
                                cube = bring_edge_to_change(cube, colors[0], colors[1])
                                cube = change_edges(cube)
                                cube = bring_edge_back(cube, colors[0], colors[1])
                                quit = True
                                break
    while not is_corners_solved(cube):
        if not is_corner_buffer(cube):
            cube = bring_corner_to_change(cube, cube[1][0], cube[0][0], cube[4][1])
            cube = change_corners(cube)
            cube = bring_corner_back(cube, cube[5][1], cube[3][3], cube[2][2])
        else:
            quit = False
            for s in range(6):
                if not quit:
                    for b in range(4):
                        if cube[s][b] != cube[s][8]:
                            colors = get_corner_colors(s, b)
                            if not (colors == 'owb' or colors == 'wbo' or colors == 'bow'):
                                cube = bring_corner_to_change(cube, colors[0], colors[1], colors[2])
                                cube = change_corners(cube)
                                cube = bring_corner_back(cube, colors[0], colors[1], colors[2])
                                quit = True
                                break
    print('\n')
    return cube
