#!/usr/local/bin/python3
# coding: utf-8

import time

def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while(a < n):
        print(a, end=' ')
        a, b = b, a+b
    print()

a=1e300
print("List of Fibonacci numbers up to {:1.0e} :".format(a))
t_begin=time.time()
fib(a)
t_end=time.time()
print("Execution time: {:.3} seconds.".format(t_end-t_begin))
