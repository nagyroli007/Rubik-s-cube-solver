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
    for i in range(f):
        r = randint(0, 12)
        if r == 0:
            cube = rotations.rotate_U(cube)
            print("U ", end='')
        elif r == 1:
            cube = rotations.rotate_U_counter(cube)
            print("U' ", end='')
        elif r == 2:
            cube = rotations.rotate_L(cube)
            print("L ", end='')
        elif r == 3:
            cube = rotations.rotate_L_counter(cube)
            print("L' ", end='')
        elif r == 4:
            cube = rotations.rotate_F(cube)
            print("F ", end='')
        elif r == 5:
            cube = rotations.rotate_F_counter(cube)
            print("F' ", end='')
        elif r == 6:
            cube = rotations.rotate_R(cube)
            print("R ", end='')
        elif r == 7:
            cube = rotations.rotate_R_counter(cube)
            print("R' ", end='')
        elif r == 8:
            cube = rotations.rotate_B(cube)
            print("B ", end='')
        elif r == 9:
            cube = rotations.rotate_B_counter(cube)
            print("B' ", end='')
        elif r == 10:
            cube = rotations.rotate_D(cube)
            print("D ", end='')
        elif r == 11:
            cube = rotations.rotate_D_counter(cube)
            print("D' ", end='')
    print("\n")
    return cube


cube = cube_to_solved()
cube = scramble(cube, 16)
print_cube(cube)
cube = solving.solve(cube)
print_cube(cube)



