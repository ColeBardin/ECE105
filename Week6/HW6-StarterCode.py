import numpy as np

"""
YOUR FULL NAME HERE
YOUR STUDENT ID HERE

ASSIGNMENT: COMPLETE function place() below
"""

"""
ECE 105: Programming for Engineers 2
Created September 8, 2020
Steven Weber
n queens problem starter code

This code finds a solution to the n queens problem, for n > 3
"""

# create an n x n board
def board(n):
	# create an n x n numpy array; each position = False
	return np.full((n, n), False)

# check if board is valid
def valid(loc):
	# check that each row is unique
	if len(loc) > len(set(loc[:,0])): return False
	# check that each column is unique
	if len(loc) > len(set(loc[:,1])): return False
	# check that each forward diagonal is unique
	# all squares on the same forward diagonal have same diff r-c
	if len(loc) > len(set([l[0]-l[1] for l in loc])): return False
	# check that each reverse diagonal is unique
	# all squares on the same reverse diagonal have same sum r+c
	if len(loc) > len(set([l[0]+l[1] for l in loc])): return False
	# passed all tests, return True
	return True

# return True if board is "open" at position (r,c)
def is_open(loc, r, c):
	# check if row r is already occupied
	if r in set(loc[:,0]): return False
	# check if column c is already occupied
	if c in set(loc[:,1]): return False
	# check if forward diagonal r-c is already occupied
	if r - c in set([l[0]-l[1] for l in loc]): return False
	# check if reverse diagonal r+c is already occupied
	if r + c in set([l[0]+l[1] for l in loc]): return False
	# position (r,c) is not occupied, return True
	return True

# find all open positionss (aop)
def all_open_pos(loc, n):
	# initialize list of all open positions
	aop = []
	# iterate over all positions (r,c)
	for r in range(n):
		for c in range(n):
			# if position is open, add it to aop
			if is_open(loc, r, c): aop.append((r,c))
	# return list of all open positions
	return aop

# print the board
def print_board(b):
	# iterate over all row positions r
	for r in range(np.shape(b)[0]):
		print("|",end='')
		# iterate over all column positions c
		for c in range(np.shape(b)[1]):
			# print "Q" for queen, "." if empty
			if b[r,c]: print("Q ",end='')
			else: print(". ",end='')
		print("|")

"""
COMPLETE:
place(b) tries all possible ways to place a queen on board b

Steps:
1. loc: locations of queens on board
2. n: board size
3. return True if all queens have been placed
4. find all open positions (aop)
5. if no open positions, return False
6. consider each open position p
	6a. place a queen at position p on b
	6b. if place(b) is True, return True
	6c. place(b) doesn't work, unset it
7. no open positions in aop work, return False
"""
# place queen
def place(b):
	# 1. loc: locations of queens on board
	loc = np.argwhere(b==1)
	# 2. n: board size
	n = 8
	# 3. return True if all queens have been placed
	if valid(loc) and len(loc)==n: return True
	# 4. find all open positions (aop)
	aop = all_open_pos(loc,n)
	# 5. if no open positions, return False
	if not len(aop): return False
	# 6. consider each open position p
	for p in aop:
		# 6a. place a queen at position p on b
		b[p[0],p[1]] = 1
		# 6b. if place(b) is True, return True
		if place(b): return True
		# 6c. place(b) doesn't work, unset it
		else: b[p[0],p[1]] = 0
	# 7. no open positions in aop work, return False
	return False

# main function
if __name__ == "__main__":
	# select the board size
	n = 8
	# create the board
	b = board(n)
	# place the queens on the board
	place(b)
	# print the solution
	print("Solution:")
	print_board(b)
	# verify the solution is valid
	loc = np.argwhere(b == 1)
	print("Valid: {}".format(len(loc) == n and valid(loc)))
