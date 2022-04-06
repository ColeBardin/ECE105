import matplotlib.pyplot as plt

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE pmf_and_cdf function below
"""

"""
ECE 105: Programming for Engineers 2
Created September 7, 2020
Steven Weber
Collatz empirical PMF and CDF starter code

This code plots the empirical PMF and CDF of Collatz sequence lengths
"""

"""
COMPLETE:
pmf_and_cdf takes a dictionary data with numerical keys and values
and produces the empirical PMF and CDF for that data
Steps:
1. v_set: set of distinct values found in data
2. tal1: count occurrences each value occurs in data
3. pmf: the tally divided by the length of the data
4. tal2: # data points with value <= each value in data
5. cdf: fraction of data points <= each value in data
6. return both the PMF and CDF
"""
# empirical PMF and CDF for numerical data (in a list)
def pmf_and_cdf (data):
	# 1. v_set: set of distinct values found in data
	v_set = list(set(data))
	pass
	# 2. tal1: count occurrences each value occurs in data
	tal1 = {n:(data.count(n)) for n in v_set }
	pass
	# 3. pmf: the tally divided by the length of the data
	pmf = {key:(value/len(data)) for (key,value) in tal1.items()}
	pass
	# 4. tal2: # data points with value <= each value in data
	tal2 = {n:len([xe for xe in data if xe<=n]) for n in data}
	pass
	# 5. cdf: fraction of data points <= each value in data
	cdf = {key:value/(len(tal2)) for (key,value) in tal2.items()}
	pass
	# 6. return both the PMF and CDF
	return pmf, cdf

# Collatz function
def c(n):
	if n % 2: return 3 * n + 1
	else: return n//2

# compute Collatz sequence lengths for n in n_set
def lcall(n_set):
	# "primary" length Collatz (lc) function: check cache
	def lc(n):
		if n not in cache: cache[n] = _lc(n)
		return cache[n]
	# "auxiliary" lc function, length is 1 + lc(c(n))
	def _lc(n):
		if n == 1: return 1
		else: return 1 + lc(c(n))
	# initialize the cache
	cache = {}
	# call lc(n) for each value of n in n_set
	for n in n_set: lc(n)
	# return the cache
	return {n : cache[n] for n in n_set}

# plot_pmf_and_cdf
def plot_pmf_and_cdf(x, y1, y2, xlabel, ylabel1, ylabel2, title, filename):
	# get the axes ax1
	fig, ax1 = plt.subplots()
	# set labels for x-axis and left-side y-axis
	ax1.set_xlabel(xlabel)
	ax1.set_ylabel(ylabel1, color='blue')
	# plot y1 data stem plot
	ax1.stem(x, y1)
	# show the axis ticks
	ax1.tick_params(axis='y')
	# use the Matplotlib twinx command to create 2nd y-axis
	ax2 = ax1.twinx()
	# set label for right-side y-axis
	ax2.set_ylabel(ylabel2, color='red')
	# plot y2 data using "steps-post" style, in red
	ax2.plot(x, y2, drawstyle='steps-post', color='red')
	# show the axis ticks
	ax2.tick_params(axis='y')
	# sest title, use tight_layout, save the file
	plt.title(title)
	fig.tight_layout()
	plt.savefig(filename)

# main function
if __name__ == "__main__":
	# specify ranges of integers to test
	n_max_set = [10, 100, 1000, 10000, 100000]

	# provide plot labels
	xlbl = 'Collatz sequence lengths'
	ylbl1 = 'PMF of sequence lengths'
	ylbl2 = 'CDF of sequence lengths'
	title_base = 'PMF, CDF of Collatz sequence lengths up to n = '
	filename_base = 'Lab5-SampleOutput-'

	# iterate over each value of n_max in n_max_set
	for n_max in n_max_set:
		# get the sequence length
		data_dict = lcall(range(1,n_max+1))
		data_vals = list(data_dict.values())
		# call cdf_and_pmf method using values from data
		pmf, cdf = pmf_and_cdf(data_vals)
		# plot the empirical CDF
		x = sorted(list(pmf.keys())) # set of values in data
		y1 = [pmf[xe] for xe in x] # PMF (could use pmf.values())
		y2 = [cdf[xe] for xe in x] # CDF (could use cdf.values())
		title = title_base + str(n_max)
		filename = filename_base + str(n_max) + '.pdf'
		plot_pmf_and_cdf(x, y1, y2, xlbl, ylbl1, ylbl2, title, filename)
