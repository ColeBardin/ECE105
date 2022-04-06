import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation
import networkx as nx
import random

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE function update below
"""

"""
ECE 105: Programming for Engineers 2
Created September 9, 2020
Steven Weber
Schelling dynamics 2-dim starter code

This code runs and plots Schelling dynamics on a 2-dim plot
"""

# initialize state to alternate
def alt_init_state(G):
	# location (r,c) is True if r+c is even, else False
	return {v: True if (v[0]+v[1])%2==0 else False for v in G.nodes() }

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
		if len(d) > 2: uv[state[v]].append(v)
	# return lists of unsatisfied vertices
	return uv

# state evolution
def state_evol(G, state):
	# find the unsatisfied vertices (uv)
	uv = find_unsat_vertices(G, state)
	# check if pair of unsat. vertices to swap exists
	uvp_exists = len(uv[0]) > 0 and len(uv[1]) > 0
	# sv: pairs swapped vertices, initially empty
	sv = []
	# stop if no more unsat. vertex pairs, or Tmax iterations
	while uvp_exists:
		# pick random unsat. vertex with state 0 (1)
		u, v = random.choice(uv[0]), random.choice(uv[1])
		# record these vertices as the ones to be swapped
		sv.append([u,v])
		# swap the state of these vertices
		state[u], state[v] = True, False
		# update list of unsatisfied vertices
		uv = find_unsat_vertices(G, state)
		# update uvp_exists indicator
		uvp_exists = len(uv[0]) > 0 and len(uv[1]) > 0
	# return state list and list of swapped vertices
	return sv

# convert state dictionary s to 2-dim matrix
def state_to_mat(s, n):
	return np.array([[1 if s[(r,c)] else 0 for c in range(n)] for r in range(n)])

"""
COMPLETE:
update(i, im, sv)
"""
# update: used by FuncAnimation to update the figure
def update(i, im, sv):
	# 1. a: use im.get_array() to get image array a from im
	a = im.get_array()
	# 2. get the pair of swapped vertices in frame i from sv
	u, v = sv[i][0], sv[i][1]
	# 3. update a at u[0],u[1] to be 1, and at v[0],v[1] to be 0
	a[u[0],u[1]], a[v[0],v[1]] = 1, 0
	# 4. use im.set_array(a) to set the image array
	im.set_array(a)
	# 5. call plt.title() to show the frame index i+1
	plt.title('{}/{}'.format(i+1,len(sv)))
	# 6. return the updated image [im]
	return [im]

# plot evolution
def plot_evol(sm, sv):
	# define a colormap using Matplotlib's colors
	# 0 : white (w), 1 : black (k)
	cmap = colors.ListedColormap(['w','k'])
	# use imshow with colormap to show state matrix sm
	fig = plt.figure()
	plt.gca().set_aspect('equal')
	plt.axis('off')
	im = plt.imshow(sm, cmap=cmap, interpolation='nearest')
	ani = FuncAnimation(fig, update, frames=range(len(sv)), fargs=(im, sv,), interval=1, blit=True, repeat=False)
	plt.show()

# plot the state
def plot_state(state):
	plt.figure()
	plt.gca().set_aspect('equal')
	plt.axis('off')
	cmap = colors.ListedColormap(['w','k'])
	plt.imshow(state, cmap=cmap, interpolation='nearest')
	plt.show()

# main function
if __name__ == "__main__":
	# n: length of each side of the square
	n = 30
	# create the n x n 2d grid graph
	G=nx.grid_2d_graph(n,n)
	# initialize the state
	state = alt_init_state(G)
	# convert state to a matrix sm
	sm = state_to_mat(state, n)
	# plot initial state
	plot_state(sm)
	# get swapped vertices list (sv)
	sv = state_evol(G, state)
	# animate the evolution
	plot_evol(sm, sv)





