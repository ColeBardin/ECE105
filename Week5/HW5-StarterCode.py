import matplotlib.pyplot as plt

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE function XXX below
"""

"""
ECE 105: Programming for Engineers 2
Created September 8, 2020
Steven Weber
Collatz sequence visualization starter code

This code plots Collatz sequences
"""

# Collatz function
def c(n):
	if n % 2: 
		return 3 * n + 1
	else: 
		return n//2

"""
COMPLETE:
cs(n_set) returns the Collatz sequence for each n in n_set
Your code should use the memoization paradigm as shown in lecture and in lab.

a) Create an empty dictionary named cache

b) Define a "primary" function (inside cs) named mc(n) that i) checks if n is in cache, and if not calls the "auxiliary" function named _mc(n) to save to cache, then returns cache[n]

c) The auxiliary function _mc(n) should return the list [1] for n=1.  For n > 1, it should return the list beginning with n and containing the Collatz sequence for c(n)

d) cs shoud call mc(n) for each n, then return the key : value pairs in cache for keys n in n_set
"""
# compute Collatz sequences for n in n_set
def cs(n_set):
	# "primary" Collatz sequence (mc) function
	def mc(n):
		if n not in cache:	cache[n] = _mc(n)
		return cache[n]
	# "auxiliary" Collatz sequence function
	def _mc(n):
		if n==1:	return [1]
		else:	return [n] + mc(c(n))

	# initialize the cache
	cache = {}
	# call mc(n) for each value of n in n_set
	return {n:mc(n) for n in n_set}
	#return cache

# Collatz sequence plot (2 variations, indexed by Boolean v)
def csp(csd, v, xlbl, ylbl, title, filename):
	# starting index list (sil)
	# start at cs[0] if v is True, else start at 1
	# v True: each sequence s(n) begins at the x-axis value of n
	# v False: each sequence s(n) begins at the x-axis value of 1
	sil = [cs[0] if v else 1 for cs in csd.values()]
	# plot the lines (plt.plot) and points (plt.scatter)
	plt.figure()
	[plt.plot(range(si,si+len(cs)), cs, label=cs[0]) for cs, si in zip(csd.values(),sil)]
	[plt.scatter(range(si,si+len(cs)), cs) for cs, si in zip(csd.values(),sil)]
	# decorate plot: axis labels, title, legend, grid
	plt.xlabel(xlbl)
	plt.ylabel(ylbl)
	plt.title(title)
	plt.legend()
	plt.grid()
	plt.savefig(filename)

# main function
if __name__ == "__main__":
	# strings for decorating the plots
	xlbl = 'Starting value (n)'
	ylbl = 'Collatz sequence s(n)'
	title = 'Collatz sequence vs. starting value'

	# compute all Collatz sequences s(n) for n=1,...,n_max1
	n_max1 = 10
	csd1 = cs(range(1,n_max1+1))
	# plot all Collatz sequences s(n) for n=1,...,n_max1
	# have sequences start at x = n (v1) and at x = 1 (v2)
	filename1 = 'HW5-SampleOutput-1.pdf'
	filename2 = 'HW5-SampleOutput-2.pdf'
	csp(csd1, True, xlbl, ylbl, title, filename1)
	csp(csd1, False, xlbl, ylbl, title, filename2)

	# compute all Collatz sequences s(n) for n=1,...,n_max2
	n_max2 = 100
	csd2 = cs(range(1,n_max2+1))
	# find the longest length sequence
	cslm = max([len(cs) for cs in csd2.values()])
	# extract the sequences in csd with longest length
	csm = {n: cs for n, cs in csd2.items() if len(cs) == cslm}
	# plot them, all starting at x = 1




