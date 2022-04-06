import numpy as np
import random
import matplotlib.pyplot as plt

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE random_point function below
"""

"""
ECE 105: Programming for Engineers 2
Created September 9, 2020
Steven Weber
Chaos game starter code

This code plays the "chaos game" to create fractal images
"""

# return the point on the unit circle at angle theta
def unit_circle(theta):
	return np.array([np.cos(theta), np.sin(theta)])

# return vnum uniformly spaced points on the unit circle
def create_vertices(vnum):
	theta = [2 * k * np.pi / vnum for k in range(vnum)]
	return unit_circle(np.array(theta)).T

"""
COMPLETE:
class random_point has a constructor and a method
1. constructor sets (vertices, f, rule) as properties
2. method next_point uses (pc, vci) to set next point

Constructor (__init__):
1. add vertices, f, rule as properties of each object

Method (next_point): take arguments (self, pc, vci)
pc: the current point
vci: the index of the current vertex

Steps:
1. select random vertex vr (use rule to return list of eligible next vertex indices)
2. return convex combination of vr and pc, and vri
"""
# class random point
class random_point:
	# constructor: set attributes vertices, f, and rule
	def __init__(self, v, f, rule):
		self.v = v
		self.f = f
		self.rule = rule

	# method: next_point(pc, vci)
	def next_point(self,pc,vci):
		# 1. select random vertex vr
		# use rule to return list of eligible next vertex indices
		vri = random.choice(self.rule(len(self.v),vci))
		# 2. return convex combination of vr and pc, and vri
		return (1-self.f)*pc+self.f*self.v[vri], vri

# chaos game
def chaos_game(p0, v, f, inum, rule):
	p = [p0] #initialize list of points with p0
	vci = 0 # initialize vertex to be v[0]
	rp = random_point(v, f, rule) # call class constructor
	# repeatedly select next point using last point as input
	for _ in range(inum):
		pt, vci = rp.next_point(p[-1], vci)
		p.append(pt)
	return np.array(p) # return points as numpy array

# plot_pts
def plot_pts(p, v, filename):
	plt.figure()
	plt.scatter(p[:,1],p[:,0], s=0.01)	# plot the points
	plt.scatter(v[:,1],v[:,0], s=5)# draw the vertices
	plt.gca().set_aspect('equal') # ensure aspect ratio is one
	plt.savefig(filename)
	plt.show()
	
# rule 0: return all vertices
def rule0(n,vci): return range(n)
# rule 1: return all vertices except the current one
def rule1(n,vci): return list(range(0,vci))+list(range(vci+1,n))
# rule 2: for a square, n=4, return the two neighbors
def rule2(n, vci):
	if n == 4 and vci == 0: return [0,1,3]
	elif n == 4 and vci == 1: return [0,1,2]
	elif n == 4 and vci == 2: return [1,2,3]
	elif n == 4 and vci == 3: return [0,2,3]
	else: print('error')

# main function
if __name__ == "__main__":

	# set common parameters for all simulations
	p0 = np.zeros(2) # initial point at the origin
	inum = 100000 # number of points / iterations

	# Example 1: Sierpinski triangle
	vnum = 3 # number of vertices in polyhedron
	f = 1/2	# fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-1.pdf'
	v = create_vertices(vnum) # create the vertices
	p = chaos_game(p0, v, f, inum, rule0) # generate the points
	plot_pts(p, v, filename) # plot the points

	# Example 2: square, f=1/2, rule1 (new point != old point)
	vnum = 4 # number of vertices in polyhedron
	f = 1/2	# fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-2.pdf'
	v = create_vertices(vnum) # create the vertices
	p = chaos_game(p0, v, f, inum, rule1) # generate the points
	plot_pts(p, v, filename) # plot the points

	# Example 3: pentagon snowflake, version 1
	vnum = 5 # number of vertices in polyhedron
	f = 1/2	# fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-3.pdf'
	v = create_vertices(vnum) # create the vertices
	p = chaos_game(p0, v, f, inum, rule1) # generate the points
	plot_pts(p, v, filename) # plot the points

	# Example 4: Sierpinski carpet
	v = np.array([[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]) # vertices
	f = 2/3	# fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-4.pdf'
	p = chaos_game(p0, v, f, inum, rule0) # generate the points
	plot_pts(p, v, filename) # plot the points

	# Example 5: pentagon snowflake, version 2
	vnum = 5 # number of vertices in polyhedron
	f = 2/(1+np.sqrt(5)) # fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-5.pdf'
	v = create_vertices(vnum) # create the vertices
	p = chaos_game(p0, v, f, inum, rule0) # generate the points
	plot_pts(p, v, filename) # plot the points

	# Example 6: square, f=1/2, rule 2: any vertex other than opposite
	vnum = 4 # number of vertices in polyhedron
	f = 1/2 # fraction between current and vertex for next
	filename = 'Lab7-SampleOutput-6.pdf'
	v = create_vertices(vnum) # create the vertices
	p = chaos_game(p0, v, f, inum, rule2) # generate the points
	plot_pts(p, v, filename) # plot the points
