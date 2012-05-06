#!/usr/bin/python
import sys

# data

ones = { 0 : 0, 1 : 1 }

# functions

def onesc( s ):
	if( s in ones ):
		return ones[ s ]
	else:
		r = onesc( s / 2 )
		if( s % 2 != 0 ):
			r = r + 1
		ones[ s ] = r
		return r

def yuki( n ):
	m = 0
	for i in range( 1, n / 2 + 2 ):
		m = max( m, onesc( i ) + onesc( n - i ) )
	return m

# main

C = long(sys.stdin.readline())

i = long(1)
for line in sys.stdin:
	print "Case #{}: {}".format( i, yuki( int( line ) ))
	i = i + 1
