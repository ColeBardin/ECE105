import numpy as np
import random
import matplotlib.pyplot as plt

"""
Cole Bardin 14422557

ASSIGNMENT: COMPLETE function chaos_game below
"""

"""
ECE 105: Programming for Engineers 2
Created September 9, 2020
Steven Weber
Barnsley fern starter code

This code draws the Barnsley fern fractal

References:
1) "Wikipedia: Barnsley Fern"
https://en.wikipedia.org/wiki/Barnsley_fern

2) "MathImages: Barnsley Fern"
https://mathimages.swarthmore.edu/index.php/Barnsley_Fern

3) "YouTube: Barnsley fern"
https://www.youtube.com/watch?v=iGMGVpLMtMs
"""

# class affine_transformation:
# attributes: M: a 2 x 2 array and b: a 2 x 1 vector
# methods: transform: compute point M z + b
class affine_transformation():
	# constructor: set attributes M and b using arguments
	def __init__(self, a, b, c, d, e, f):
		self.M = np.array([[a,b],[c,d]])
		self.b = np.array([[e],[f]])
	# method: apply the transform to the point z given in argument
	def transform(self, z): return np.dot(self.M, z) + self.b

"""
COMPLETE:
chaos_game(p0, w, f, inum)
Inputs:
p0: initial point (x0,y0)
w: weights for random selection among f
f: list of affine transformations
inum: number of iterations / points

Steps:
1. initialize empty list of points for each transform
2. initialize current point cp as initial point p0
3. repeatedly select next point using last point as input
	3a. chooses a random index ir using weights w
	3b. update cp using the corresponding transform
	3c. append cp to the appropriate list of points
4. return points
"""
# chaos_game: generate the points
def chaos_game(p0, w, f, inum):
	# 1. initialize empty list of points for each transform
	pE = [ [], [], [], [] ]
	# 2. initialize current point cp as initial point p0
	cp = p0
	# 3. repeatedly select next point using last point as input
	for _ in range(inum):
		# 3a. chooses a random index ir using weights w
		ir = random.choices([0,1,2,3], weights=w)[0]
		# 3b. update cp using the corresponding transform
		cp = f[ir].transform(cp)
		# 3c. append cp to the appropriate list of points
		pE[ir].append(cp)
	# 4. return points
	return pE

# plot points
def plot_pts(p, filename):
	pa = [np.array(pi) for pi in p]
	# choose the colors for the points under the four transforms
	colors = ['b','g','r','k']
	plt.figure()
	# plot the points
	[plt.scatter(pai[:,1],pai[:,0], s=0.01, c=ci) for pai,ci in zip(pa,colors)]
	plt.gca().set_aspect('equal') # ensure aspect ratio is one
	plt.savefig(filename)
	plt.show()

# main function
if __name__ == "__main__":
	# w: weights on the four affine transformations f1, f2, f3, f4
	w = np.array([0.01, 0.85, 0.07, 0.07])
	# four affine transformations, each w/ 2x2 mat. M & 1x2 vec. b
	f1 = affine_transformation( 0.00, 0.00, 0.00, 0.16, 0.00, 0.00)
	f2 = affine_transformation( 0.85, 0.04,-0.04, 0.85, 0.00, 1.60)
	f3 = affine_transformation( 0.20,-0.26, 0.23, 0.22, 0.00, 1.60)
	f4 = affine_transformation(-0.15, 0.28, 0.26, 0.24, 0.00, 0.44)
	f = [f1, f2, f3, f4]

	# p0 = (0,0): initial point
	p0 = np.array([[0],[0]])
	# inum: number of iterations
	inum = 10000
	# filename for output plot
	filename = 'HW7-SampleOutput.pdf'

	# create the points p using chaos_game
	p = chaos_game(p0, w, f, inum)
	# plot them using plot_pts
	plot_pts(p, filename)
