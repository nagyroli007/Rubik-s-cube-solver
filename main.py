from random import randint
import rotations
import solving


# Brings the cube to the solved state (by setting the colors of the blocks)
def cube_to_solved():
    cube = ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']
    colors = ('w', 'o', 'g', 'r', 'b', 'y')
    for s in range(6):
        for b in range(9):
            cube[s][b] = colors[s]
    return cube


# Printing out the current state of the cube
def print_cube(cube):
    print("    " + cube[0][0] + cube[0][4] + cube[0][1])
    print("    " + cube[0][7] + cube[0][8] + cube[0][5])
    print("    " + cube[0][3] + cube[0][6] + cube[0][2])
    print(cube[1][0] + cube[1][4] + cube[1][1] + " " + cube[2][0] + cube[2][4] + cube[2][1] + " " + cube[3][0] + cube[3][4] + cube[3][1] + " " + cube[4][0] + cube[4][4] + cube[4][1])
    print(cube[1][7] + cube[1][8] + cube[1][5] + " " + cube[2][7] + cube[2][8] + cube[2][5] + " " + cube[3][7] + cube[3][8] + cube[3][5] + " " + cube[4][7] + cube[4][8] + cube[4][5])
    print(cube[1][3] + cube[1][6] + cube[1][2] + " " + cube[2][3] + cube[2][6] + cube[2][2] + " " + cube[3][3] + cube[3][6] + cube[3][2] + " " + cube[4][3] + cube[4][6] + cube[4][2])
    print("    " + cube[5][0] + cube[5][4] + cube[5][1])
    print("    " + cube[5][7] + cube[5][8] + cube[5][5])
    print("    " + cube[5][3] + cube[5][6] + cube[5][2])
    print()


# Scrambles the cube by performing a random rotations (f times)
def scramble(cube, f):
    print("Scramble: ", end='')
    prev = -1
    streak = 0
    for i in range(f):
        r = randint(0, 12)
        # If the next equalt the previous, then add 1 to the streak
        if r == prev:
            streak += 1
            # If at least 3 in a row, delete last
            if streak >= 2:
                streak = 1
                r = -1
                i -= 1
        # If not equals the prev
        else:
            streak = 0
            # If the next is the counter part of the prev, then delete it
            if int(r / 2) == int(prev / 2):
                r = -1
                i -= 1
        if r == 0:
            cube = rotations.rotate_U(cube)
        elif r == 1:
            cube = rotations.rotate_U_counter(cube)
        elif r == 2:
            cube = rotations.rotate_L(cube)
        elif r == 3:
            cube = rotations.rotate_L_counter(cube)
        elif r == 4:
            cube = rotations.rotate_F(cube)
        elif r == 5:
            cube = rotations.rotate_F_counter(cube)
        elif r == 6:
            cube = rotations.rotate_R(cube)
        elif r == 7:
            cube = rotations.rotate_R_counter(cube)
        elif r == 8:
            cube = rotations.rotate_B(cube)
        elif r == 9:
            cube = rotations.rotate_B_counter(cube)
        elif r == 10:
            cube = rotations.rotate_D(cube)
        elif r == 11:
            cube = rotations.rotate_D_counter(cube)
        prev = r
    print("\n")
    return cube


# Returns if the positions are good for the swap algorithm
def edge_all_good(cube, a, b):
    if cube[0][7] == a and cube[1][7] == b:
        if cube[0][1] == 'w' and cube[0][2] == 'w':
            if cube[3][0] == 'r' and cube[3][1] == 'r':
                if cube[2][1] == 'g' and cube[4][0] == 'b':
                    return True
    return False


# Copies a given cube
def copy_cube(cube):
    copy = cube_to_solved()
    for x in range(6):
        for y in range(9):
            copy[x][y] = cube[x][y]
    return copy


# Will learn how to bring the edge to the swap position
def get_edge_moves(cube, a, b):
    print("get edge moves")
    prevcube = copy_cube(cube)
    t = 0
    while t < 4:
        for r in range(12):
            if r == 0:
                cube = rotations.rotate_U(cube)
            elif r == 1:
                cube = rotations.rotate_U_counter(cube)
            elif r == 2:
                cube = rotations.rotate_L(cube)
            elif r == 3:
                cube = rotations.rotate_L_counter(cube)
            elif r == 4:
                cube = rotations.rotate_F(cube)
            elif r == 5:
                cube = rotations.rotate_F_counter(cube)
            elif r == 6:
                cube = rotations.rotate_R(cube)
            elif r == 7:
                cube = rotations.rotate_R_counter(cube)
            elif r == 8:
                cube = rotations.rotate_B(cube)
            elif r == 9:
                cube = rotations.rotate_B_counter(cube)
            elif r == 10:
                cube = rotations.rotate_D(cube)
            elif r == 11:
                cube = rotations.rotate_D_counter(cube)
            if edge_all_good(cube, a, b):
                print("\n" + str(r))
                return
            cube = copy_cube(prevcube)
            print()
        t += 1
        if t == 2:
            break
        



cube = cube_to_solved()
cube = scramble(cube, 20)
print_cube(cube)
cube = solving.solve(cube)
print_cube(cube)

get_edge_moves(cube, 'y', 'o')
