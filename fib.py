#!/usr/local/bin/python3

def fib(n):
	a,b=0,1
	while(a<n):
		print(a,end=' ')
		a,b=b,a+b
	print()

fib(1e3)
