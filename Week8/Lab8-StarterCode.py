import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import networkx as nx
import random

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE state_evol function below
"""

"""
ECE 105: Programming for Engineers 2
Created September 9, 2020
Steven Weber
Schelling dynamics solution

This code runs and plots Schelling dynamics on a 1-dim plot
"""

# initialize state to alternate
def alt_init_state(G):
	# alternate states between 0 and 1
	return { v : v % 2 for v in G.nodes() }

# find unsatisfied vertices
def find_unsat_vertices(G, state):
	# init. list of unsat. vertices as two empty "sub"-lists
	uv = [[],[]]
	# iterate over the vertices in the graph:
	for v in G.nodes():
		# d: list of neighbors u of v w/ state diff. from v
		d = [u for u in G.neighbors(v) if state[v] != state[u]]
		# v unsat. if both its neighbors are different
		# add v to sublist of unsat. states for v's state
		if len(d) == 2: uv[state[v]].append(v)
	# return lists of unsatisfied vertices
	return uv

"""
COMPLETE:
state_evol(G, state) takes a graph G and an initial state
it applies the Schelling dynamics repeatedly
and returns a list of states and a list of swapped vertex pairs

Steps:
1. find the unsatisfied vertices (uv)
2. uvp_exists: True if pair of unsat. vertices to swap exists
3. sl: list of states, initialized with *copy* of state
4. sv: list of swapped vertex pairs, initially empty
5. while uvp_exists, repeatedly apply dynamics
	5a. pick random unsat. vertex pair u, v: u random choice from uv[0], v random choice from uv[1]
	5b. append vertex pair list [u,v] to sv
	5c. swap vertex states: state[u] is True, state[v] is False
	5d. sl appended with *copy* of state
	5e. uv = list of unsatisfied vertices
	5f. update uvp_exists Boolean indicator
6. return state list sl and list of swapped vertices sv
"""
# state evolution
def state_evol(G, state):
	# 1. find the unsatisfied vertices (uv)
	uv = find_unsat_vertices(G, state)
	# 2. uvp_exists: True if pair unsat. vertices to swap exists
	uvp_exists = len(uv[0]) > 0 and len(uv[1]) > 0
	# 3. sl: list of states, initialized with *copy* of state
	sl = [state.copy()]
	# 4. sv: list of swapped vertex pairs, initially empty
	sv = []
	# 5. while uvp_exists, repeatedly apply dynamics
	while uvp_exists:
		# 5a. pick random unsat. vertex pair u, v
		# u random choice from uv[0], v random choice from uv[1]
		u, v = random.choice(uv[0]), random.choice(uv[1])
		# 5b. append vertex pair list [u,v] to sv
		sv.append([u, v])
		# 5c. swap vertex states: state[u]=True, state[v]=False
		state[u], state[v] = True, False
		# 5d. sl appended with *copy* of state
		sl.append(state.copy())
		# 5e. uv = list of unsatisfied vertices
		uv = find_unsat_vertices(G, state)
		# 5f. update uvp_exists Boolean indicator
		uvp_exists = len(uv[0]) > 0 and len(uv[1]) > 0
	# 6. return state list sl and list of swapped vertices sv
	return sl, sv

# convert state list sl to matrix sm
def state_to_mat(sl, sv):
	# nr: number of rows (steps in evolution)
	# nc: number of columns (sites, vertices, nodes)
	nr, nc = len(sl), len(sl[0])
	# initialize an empty nr x nc 2-dim numpy array sm
	sm = np.empty((nr, nc), dtype=int)
	# iterate over each position (r,c):
	for r in range(nr):
		for c in range(nc):
			# sm[r,c] = 1 if sl[r][c] is True, else 0
			sm[r,c] = 1 if sl[r][c] else 0
			# sm[r,c] = 2 if vertex c swapped at time r
			if r < nr - 1 and c in sv[r]: sm[r,c] = 2
	return sm

# plot evolution
def plot_evol(sm, xlbl, ylbl, title, filename):
	# define a colormap using Matplotlib's colors
	# 0 : white (w), 1 : black (k), 2 : red (r)
	cmap = colors.ListedColormap(['w','k','r'])
	# use imshow with colormap to show state matrix sm
	plt.figure()
	plt.imshow(sm, cmap=cmap, interpolation='nearest')
	plt.xlabel(xlbl)
	plt.ylabel(ylbl)
	plt.title(title)
	plt.savefig(filename)
	plt.show()

# main function
if __name__ == "__main__":
	# n: # of vertices in graph
	n = 101
	# create the cycle graph C_n
	G=nx.cycle_graph(n)
	# initialize the state
	state = alt_init_state(G)
	# get state list (sl) and swapped vertices list (sv)
	sl, sv = state_evol(G, state)
	# convert state list sl to a matrix sm
	sm = state_to_mat(sl, sv)
	# plot the evolution
	xlbl = 'Site / vertex / node index'
	ylbl = 'State / time index'
	title = 'Schelling dynamics on cycle graph'
	filename = 'Lab8-SampleOutput.pdf'
	plot_evol(sm, xlbl, ylbl, title, filename)
