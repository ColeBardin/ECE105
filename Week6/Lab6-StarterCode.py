import numpy as np

"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE XXX function below
"""

"""
ECE 105: Programming for Engineers 2
Created September 8, 2020
Steven Weber
Sudoku solver starter code

This code solves Sudoku instances
"""

# convert '.' to 0 and characters 1,...,9 to integers
def cha_to_int(c):
    if c == '.': return 0
    elif int(c) in list(range(1,10)): return int(c)

# convert a string s to a 9 x 9 2-dim numpy array
def str_to_arr(s):
    l = [cha_to_int(c) for c in s]
    return np.array(l).reshape(9,9)

# return the first open position in the instance i
def first_open_pos(i):
    for r in range(9):
        for c in range(9):
            if i[r,c] == 0: return [r,c]
    return False

# return the block (flattened) holding row r column c in instance i
def blk(i, r, c):
    b = i[3*(r//3) : 3*(r//3+1), 3*(c//3) : 3*(c//3+1)]
    return b.flatten()

# return all available values for instance i in row r column c
# d is available if d is not used in the row, column, or block
def avail(i,r,c):
    d_l = []
    for d in range(1,10):
        if d not in i[r,:] and d not in i[:,c] and d not in blk(i,r,c):
            d_l.append(d)
    return d_l

"""
COMPLETE:
assign(i) takes a Sudoku instance i as argument, recurses by trying all possible values for the first open position it finds, and returns True if the assignment is valid

Steps:
1. fop: find the first open position (fop) in i
2. if there are none, then i is "solved", return True
3. iterate over all values d available at fop w/ avail()
    3a. assign value d to position fop in instance i
    3b. if i w/ assignment d to fop is valid, return True
4. no valid assign. of i w/ fop: "unset" pos. fop to 0
5. return False (dead end)
"""
# assign values to open positions in an instance i
def assign(i):
    # 1. fop: find the first open position (fop) in i
    fop = first_open_pos(i)
    # 2. if there are none, then i is "solved", return True
    if not fop: return True
    # 3. iterate over all values d available at fop w/ avail()
    for d in avail(i,fop[0],fop[1]):
        # 3a. assign value d to position fop in instance i
        i[fop[0],fop[1]] = d
        # 3b. if i w/ assignment d to fop is valid, return True
        if assign(i): return True
    # 4. no valid assign. of i w/ fop: "unset" pos. fop to 0
    i[fop[0],fop[1]] = 0
    # 5. return False (dead end)
    return False

# get list of the 9 blocks (flattened) in instance i
def blocks(i):
    b_l = [i[0:3,0:3], i[0:3,3:6], i[0:3,6:9], i[3:6,0:3], i[3:6,3:6], i[3:6,6:9], i[6:9,0:3], i[6:9,3:6], i[6:9,6:9]]
    return [b.flatten() for b in b_l]

# a list (set) is valid if it equals 1,...,9
def valid_set(s):
    return s == set(range(1,10))

# an instance is valid if all rows, columns, blocks are valid
def valid(i):
    # return False if there are any invalid rows
    if not all([valid_set(set(r)) for r in i]): return False
    # return False if there are any invalid columns
    if not all([valid_set(set(c)) for c in i.T]): return False
    # return False if there are any invalid blocks
    if not all([valid_set(set(b)) for b in blocks(i)]): return False
    # all rows, columns, blocks are valid, so instance is valid
    return True

# print the instance
# add vertical bars on left and right
def sud_print(i):
    for r in range(9):
        print('| ',end='')
        for c in range(9):
            print('{} '.format(i[r,c]),end='') if i[r,c] else print('  ',end='')
        print('|')

# main function
if __name__ == "__main__":
    # a sample Sudoku problem instance:
    # a string of 9 x 9 = 81 characters
    # a '.' means the position is open
    s = '.94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8'
    # convert the string s to an instance i
    i = str_to_arr(s)
    # print the instance
    print("Instance:")
    sud_print(i)
    # solve, and print the solution
    assign(i)
    print("Solution:")
    sud_print(i)
    # verify and print the verification
    print("Verify: {}".format(valid(i)))






