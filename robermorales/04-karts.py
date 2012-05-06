#!/usr/bin/python
import sys

# data

sizes = []

# functions

def schedule( R, k, G, sizes ):
	i = 0
	l = 0
	for r in range(R):
		rem = k
		gr = 0
		while( rem > 0 and sizes[ i ] <= rem and gr < G ):
			rem -= sizes[ i ]
			i = ( i + 1 ) % G
			gr = gr + 1
		l = l + k - rem
	return l

# main

N = int(sys.stdin.readline())

for i in range(N):
	( R, k, G ) = map( int, sys.stdin.readline().split() )
	sizes = map( int, sys.stdin.readline().split() )
	print schedule( R, k, G, sizes )
