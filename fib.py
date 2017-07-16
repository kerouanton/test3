#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

import time

def fib(n): # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while(a < n):
		print(a, end=' ')
		a, b = b, a+b
	print()
	
	
t=time.time()
fib(1e200)
print("Execution time:{} seconds.".format(time.time()-t))
